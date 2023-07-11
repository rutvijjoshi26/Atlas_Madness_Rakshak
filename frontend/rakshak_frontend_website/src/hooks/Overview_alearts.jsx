
import axios from "axios";
import { base_url } from "./Base_url";

export const get_overview_alerts = async () => {
  try {
    const response = await axios.get(`${base_url}api/analytics/overview/alerts`);
    const data = response.data;
    return data;
  } catch (error) {
    return error.message;
  }
};


