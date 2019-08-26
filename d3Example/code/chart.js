async function drawLineChart() {
  const dataset = await d3.json({{data|safe}});
  console.log(dataset);
};
drawLineChart();


// console.table({{data|safe}}[0]);