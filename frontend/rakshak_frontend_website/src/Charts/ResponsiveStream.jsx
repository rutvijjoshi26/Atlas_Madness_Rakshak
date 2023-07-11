import { ResponsiveStream } from "@nivo/stream";
import { useEffect, useState } from "react";
import { get_overview_stream_chart } from "../hooks/Overview_stream_chart";

const MyResponsiveStream = () => {
  const [stream_chart_data, Set_stream_chart_data] = useState([]);

  /* The `useEffect` hook is used to perform side effects in a functional component. In this case, it
  is used to fetch data for the stream chart. */
  useEffect(() => {
    const getData = async () => {
      try {
        const overview_stream_chart_data = await get_overview_stream_chart();
        Set_stream_chart_data(overview_stream_chart_data);
      } catch (error) {
        console.error("Error:", error.message);
      }
    };
    getData();
  }, []);
  console.log(stream_chart_data);
  return (
    <ResponsiveStream
      data={stream_chart_data}
      keys={["nsfw", "sfw"]}
      margin={{ top: 50, right: 110, bottom: 100, left: 60 }}
      axisTop={null}
      axisRight={null}
      axisBottom={{
        orient: "bottom",
        tickSize: 5,
        tickPadding: 5,
        tickRotation: 0,
        legend: "",
        legendOffset: 36,
      }}
      axisLeft={{
        orient: "left",
        tickSize: 5,
        tickPadding: 5,
        tickRotation: 0,
        legend: "",
        legendOffset: -40,
      }}
      enableGridX={true}
      enableGridY={false}
      curve="basis"
      offsetType="none"
      colors={{ scheme: "set1" }}
      fillOpacity={0.85}
      borderColor={{ theme: "background" }}
      defs={[
        {
          id: "dots",
          type: "patternDots",
          background: "inherit",
          color: "#2c998f",
          size: 4,
          padding: 2,
          stagger: true,
        },
        {
          id: "squares",
          type: "patternSquares",
          background: "inherit",
          color: "#e4c912",
          size: 6,
          padding: 2,
          stagger: true,
        },
      ]}
      fill={[
        {
          match: {
            id: "Paul",
          },
          id: "dots",
        },
        {
          match: {
            id: "Marcel",
          },
          id: "squares",
        },
      ]}
      enableDots={true}
      dotSize={8}
      dotColor={{ from: "color" }}
      dotBorderWidth={2}
      dotBorderColor={{
        from: "color",
        modifiers: [["darker", 0.7]],
      }}
      legends={[
        {
          anchor: "bottom-right",
          direction: "column",
          translateX: 100,
          itemWidth: 80,
          itemHeight: 20,
          itemTextColor: "#999999",
          symbolSize: 12,
          symbolShape: "circle",
          effects: [
            {
              on: "hover",
              style: {
                itemTextColor: "#000000",
              },
            },
          ],
        },
      ]}
    />
  );
};
export default MyResponsiveStream;
