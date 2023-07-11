import axios from "axios";
import { base_url } from "./Base_url";

export const get_timeline_numbers = async () => {
  try {
    const response = await axios.get(`${base_url}api/analytics/timeline/numbers`);
    const data = response.data;
    return data;
  } catch (error) {
    return error.message;
  }
};
