"""
highcharts的饼状图
"""

from sja.report import SjaReport

from jinja2 import Template

needs = """
<script src="https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
<script src="https://code.highcharts.com/highcharts.js"></script>
"""

script = Template(
    """
<script language="JavaScript">
$(document).ready(function() {
   var chart = {
       plotBackgroundColor: null,
       plotBorderWidth: null,
       plotShadow: false
   };
   var title = {
      text: '{{ chart_title }}'
   };
   var tooltip = {
      pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
   };
   var plotOptions = {
      pie: {
         allowPointSelect: true,
         cursor: 'pointer',
         dataLabels: {
            enabled: true,
            format: '<b>{point.name}%</b>: {point.percentage:.1f} %',
            style: {
               color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
            }
         }
      }
   };
   var series= [{
      type: 'pie',
      name: 'Browser share',
      data: [
      {% for i in data %}
         ['{{ i[0] }}',   {{ i[1] }}],
      {% endfor %}
      ]
   }];

   var json = {};
   json.chart = chart;
   json.title = title;
   json.tooltip = tooltip;
   json.series = series;
   json.plotOptions = plotOptions;
   $('#container').highcharts(json);
});
</script>
"""
)


def pie(report: SjaReport):
    """
    :param report: SjaReport
    :return: Highcharts Javascript
   """
    # 有可能没用但帮助思考
    key_value = report.percent_cn
    value_key = {}
    values = list(report.percent_cn.values())
    for k, v in key_value.items():
        value_key[v] = k

    values.sort()
    data = []
    for i in values:
        if i > 0:
            data.append((value_key[i], i))
        try:
            del value_key[i]
        except KeyError:
            pass

    s = 0
    for i, j in data:
        s += j
    if s > 100:
        s = s - 100
        data[-1] = (data[-1][0], data[-1][1] - s)

    return script.render(chart_title=report.program_name, data=data)
