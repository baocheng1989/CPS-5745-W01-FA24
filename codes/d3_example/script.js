const data = [
  { name: "A", value: 30 },
  { name: "B", value: 80 },
  { name: "C", value: 40 },
  { name: "D", value: 60 },
  { name: "E", value: 20 },
  { name: "F", value: 90 },
  { name: "G", value: 55 },
];

const windowWidth = window.innerWidth;
const windowHeight = window.innerHeight;

console.log(windowWidth, windowHeight);

const svg = d3.select("#bar-chart");
// const width = +svg.attr("width") || windowWidth;
// const height = +svg.attr("height") || (windowHeight/2);
// svg.attr("width", windowWidth+'px').attr("height", windowHeight/2+'px');
const margins = { top: 30, right: 30, bottom: 40, left: 40 };

const x = d3
  .scaleBand()
  .domain(data.map((d) => d.name))
  .range([margins.left, width - margins.right])
  .padding(0.1);

const y = d3
  .scaleLinear()
  .domain([0, d3.max(data, (d) => d.value)])
  .range([height - margins.bottom, margins.top]);

svg
  .append("g")
  .attr("transform", `translate(0,${height - margins.bottom})`)
  .call(d3.axisBottom(x))
  .attr("font-size", "12px");

svg
  .append("g")
  .attr("transform", `translate(${margins.left},0)`)
  .call(d3.axisLeft(y))
  .attr("font-size", "12px");

svg
  .selectAll(".bar")
  .data(data)
  .enter()
  .append("rect")
  .attr("class", "bar")
  .attr("x", (d) => x(d.name))
  .attr("y", (d) => y(d.value))
  .attr("width", x.bandwidth())
  .attr("height", (d) => y(0) - y(d.value));

const tooltip = d3.select("#tooltips");

svg
  .selectAll(".bar")
  .on("mouseover", (event, d) => {
    tooltip.style("visibility", "visible").text(`Value: ${d.value}`);
    d3.select(event.currentTarget).style("fill", "orange");
  })
  .on("mousemove", (event) => {
    tooltip
      .style("top", event.pageY - 20 + "px")
      .style("left", event.pageX + 10 + "px");
  })
  .on("mouseout", (event) => {
    tooltip.style("visibility", "hidden");
    d3.select(event.currentTarget).style("fill", "steelblue");
  });
