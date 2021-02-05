"""
highcharts的饼状图
"""

try:
    from jinja2 import Template
except ModuleNotFoundError:
    pass

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
      {% for k, v in data.items() %}
         ['{{ k }}',   {{ v }}],
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

html = Template(
    """
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8"/>
    <title>scratch程序分析器</title>
    {{ needs }}
</head>
<body>
{{ pie }}
</body>    
    """
)


def pie(scratch):
    """
    :param scratch: Scratch对象，被统计过的
    :return: Highcharts Javascript
   """

    return script.render(
        chart_title=scratch.filename,
        data=scratch.statistic.percent_cn
    )


def full_html_pie(scratch):
    """
    生成pie的完整HTML
    :param scratch: Scratch对象，被统计过的
    :return: HTML
    """
    return html.render(
        needs=needs,
        pie=pie(scratch)
    )
