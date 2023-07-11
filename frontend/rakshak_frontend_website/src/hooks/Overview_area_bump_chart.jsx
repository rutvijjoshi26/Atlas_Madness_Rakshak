import axios from "axios";
import { base_url } from "./Base_url";

export const get_overview_area_bump_chart_data = async () => {
  try {
    const response = await axios.get(`${base_url}api/analytics/overview/bump_chart`);
    const data = response.data;
    return data;
  } catch (error) {
    return error.message;
  }
};  


