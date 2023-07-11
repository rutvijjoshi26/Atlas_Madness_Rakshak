
import axios from "axios";
import { base_url } from "./Base_url";

export const get_overview_trending = async () => {
  try {
    const response = await axios.get(`${base_url}api/analytics/overview/trending`);
    const data = response.data;
    return data;
  } catch (error) {
    return error.message;
  }
};


