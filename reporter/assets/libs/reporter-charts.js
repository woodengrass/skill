// reporter-charts.js — Reporter 共用的 ECharts option builder。
// reader-template 與 portal-template 共用此檔，勿各寫一份（防 feature drift）。
// 支援：bar／hbar／line／area／pie／donut／radar／scatter／heatmap。
// 不支援的 type 回傳提示圖，不靜默畫錯。地圖已移出核心：需要地理視覺請自備圖資。
// 載入方式：<script src="libs/echarts.min.js"></script> 之後加
// <script src="libs/reporter-charts.js"></script>，呼叫 reporterChartOption(spec, ink)。
var REPORTER_PALETTE=['#4477AA','#EE6677','#228833','#CCBB44','#66CCEE','#AA3377','#BBBBBB'];
function reporterChartOption(spec,ink){
  spec=spec||{};ink=ink||'#222';
  var SUPPORTED={bar:1,hbar:1,line:1,area:1,pie:1,donut:1,radar:1,scatter:1,heatmap:1};
  var base={color:REPORTER_PALETTE,
    title:{text:spec.title||'',left:'center',textStyle:{color:ink,fontSize:15}},
    tooltip:{trigger:(spec.type==='pie'||spec.type==='donut')?'item':'axis'},
    textStyle:{color:ink,fontFamily:'Microsoft JhengHei,sans-serif'}};
  if(!SUPPORTED[spec.type]){
    return Object.assign(base,{graphic:{type:'text',left:'center',top:'middle',
      style:{text:'不支援的圖型：'+spec.type+'（改用其他圖型或表格）',fill:ink,fontSize:13}}});
  }
  if(spec.type==='pie'||spec.type==='donut'){
    var radius=spec.type==='donut'?['42%','65%']:'60%';
    return Object.assign(base,{legend:{textStyle:{color:ink}},series:[{type:'pie',radius:radius,
      data:((spec.series||[])[0].data||[]).map(function(d){return {value:+d.value||0,name:d.name}})}]});
  }
  if(spec.type==='radar'){
    return Object.assign(base,{legend:{textStyle:{color:ink}},
      radar:{indicator:(spec.indicators||[]).map(function(n){return {name:n,max:spec.max||5}})},
      series:[{type:'radar',areaStyle:{opacity:.2},
        data:(spec.series||[]).map(function(s){return {name:s.name,value:(s.data||[]).map(Number)}})}]});
  }
  if(spec.type==='scatter'){
    return Object.assign(base,{legend:{textStyle:{color:ink}},grid:{containLabel:true},
      xAxis:{type:'value',name:spec.xName||'',axisLabel:{color:ink}},
      yAxis:{type:'value',name:spec.yName||'',axisLabel:{color:ink}},
      series:(spec.series||[]).map(function(s){return {name:s.name,type:'scatter',symbolSize:10,data:s.data||[]}})});
  }
  if(spec.type==='heatmap'){
    var xs=spec.x||[],ys=spec.y||[];
    var vmax=0;(((spec.series||[])[0]||{}).data||[]).forEach(function(d){if(d[2]>vmax)vmax=d[2]});
    return Object.assign(base,{grid:{containLabel:true},
      xAxis:{type:'category',data:xs,axisLabel:{color:ink,interval:0,rotate:30}},
      yAxis:{type:'category',data:ys,axisLabel:{color:ink}},
      visualMap:{min:0,max:vmax||1,calculable:true,textStyle:{color:ink}},
      series:[{type:'heatmap',data:(((spec.series||[])[0]||{}).data||[]),
        label:{show:true},emphasis:{itemStyle:{shadowBlur:10}}}]});
  }
  var mkMark=function(){return spec.markAvg?{markLine:{symbol:'none',data:[{type:'average',name:'平均'}]}}:{}};
  var series=(spec.series||[]).map(function(s){
    var t='bar';
    if(spec.type==='line'||spec.type==='area')t='line';
    if(s.chart==='line')t='line';if(s.chart==='bar')t='bar';
    var o=Object.assign({name:s.name,type:t,data:(s.data||[]).map(function(v){return v===null?null:+v})},mkMark());
    if(spec.type==='area')o.areaStyle={opacity:.25};
    if(spec.stack)o.stack='total';
    if(typeof s.axis==='number')o.yAxisIndex=s.axis;
    return o;
  });
  var dual=series.some(function(s){return s.yAxisIndex===1});
  var yAx=dual?[{type:'value',axisLabel:{color:ink}},{type:'value',axisLabel:{color:ink}}]:{type:'value',axisLabel:{color:ink}};
  var cat={type:'category',data:spec.x||[],axisLabel:{color:ink}};
  var isH=spec.type==='hbar';
  return Object.assign(base,{legend:{textStyle:{color:ink}},grid:{containLabel:true},
    xAxis:isH?{type:'value',axisLabel:{color:ink}}:cat,
    yAxis:isH?cat:yAx,series:series});
}
