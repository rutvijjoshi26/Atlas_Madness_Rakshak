import { ResponsiveAreaBump } from "@nivo/bump";
import { useEffect, useState } from "react";
import { get_overview_area_bump_chart_data } from "../hooks/Overview_area_bump_chart";
const data = [
  {
    id: "JavaScript",
    data: [
      {
        x: 2000,
        y: 30,
      },
      {
        x: 2001,
        y: 14,
      },
      {
        x: 2002,
        y: 22,
      },
      {
        x: 2003,
        y: 25,
      },
      {
        x: 2004,
        y: 15,
      },
      {
        x: 2005,
        y: 26,
      },
    ],
  },
  {
    id: "ReasonML",
    data: [
      {
        x: 2000,
        y: 23,
      },
      {
        x: 2001,
        y: 13,
      },
      {
        x: 2002,
        y: 13,
      },
      {
        x: 2003,
        y: 18,
      },
      {
        x: 2004,
        y: 29,
      },
      {
        x: 2005,
        y: 11,
      },
    ],
  },
  {
    id: "TypeScript",
    data: [
      {
        x: 2000,
        y: 29,
      },
      {
        x: 2001,
        y: 14,
      },
      {
        x: 2002,
        y: 19,
      },
      {
        x: 2003,
        y: 23,
      },
      {
        x: 2004,
        y: 11,
      },
      {
        x: 2005,
        y: 23,
      },
    ],
  },
  {
    id: "Elm",
    data: [
      {
        x: 2000,
        y: 26,
      },
      {
        x: 2001,
        y: 18,
      },
      {
        x: 2002,
        y: 26,
      },
      {
        x: 2003,
        y: 12,
      },
      {
        x: 2004,
        y: 27,
      },
      {
        x: 2005,
        y: 18,
      },
    ],
  },
  {
    id: "CoffeeScript",
    data: [
      {
        x: 2000,
        y: 18,
      },
      {
        x: 2001,
        y: 24,
      },
      {
        x: 2002,
        y: 18,
      },
      {
        x: 2003,
        y: 27,
      },
      {
        x: 2004,
        y: 14,
      },
      {
        x: 2005,
        y: 14,
      },
    ],
  },
];

const MyResponsiveAreaBump = () => {
  const [bump_chart_data, Set_bump_chart_data] = useState([]);

  useEffect(() => {
    const getData = async () => {
      try {
        const overview_bump_chart_data =
          await get_overview_area_bump_chart_data();
        Set_bump_chart_data(overview_bump_chart_data);
      } catch (error) {
        console.error("Error:", error.message);
      }
    };
    getData();
  }, []);
  const filtered_data_bump = bump_chart_data.filter(
    (item) => item.data.length > 0
  );

  return (
    <ResponsiveAreaBump
      data={filtered_data_bump}
      margin={{ top: 40, right: 100, bottom: 40, left: 100 }}
      spacing={8}
      colors={{ scheme: "nivo" }}
      blendMode="multiply"
      defs={[
        {
          id: "dots",
          type: "patternDots",
          background: "inherit",
          color: "#38bcb2",
          size: 4,
          padding: 1,
          stagger: true,
        },
        {
          id: "lines",
          type: "patternLines",
          background: "inherit",
          color: "#eed312",
          rotation: -45,
          lineWidth: 6,
          spacing: 10,
        },
      ]}
      fill={[
        {
          match: {
            id: "CoffeeScript",
          },
          id: "dots",
        },
        {
          match: {
            id: "TypeScript",
          },
          id: "lines",
        },
      ]}
      startLabel="id"
      endLabel="id"
      axisTop={{
        tickSize: 5,
        tickPadding: 5,
        tickRotation: 0,
        legend: "",
        legendPosition: "middle",
        legendOffset: -36,
      }}
      axisBottom={{
        tickSize: 5,
        tickPadding: 5,
        tickRotation: 0,
        legend: "",
        legendPosition: "middle",
        legendOffset: 32,
      }}
    />
  );
};

export default MyResponsiveAreaBump;
