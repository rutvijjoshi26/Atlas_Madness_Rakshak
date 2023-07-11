export const getFilteredData = (data, typeOfFile) => {
  if (!data) {
    return null;
  }
  const { counts, averages, growth_rates } = data;
  const filteredCounts = counts
    ? counts.find((item) => item.file_type === typeOfFile)
    : null;
  const filteredAverages = averages
    ? averages.find((item) => item.file_type === typeOfFile)
    : null;
  const filteredGrowthRate = growth_rates
    ? growth_rates.find((item) => item.type_of_file === typeOfFile)
    : null;

  return {
    counts: filteredCounts ? filteredCounts.total_files : 0,
    averages: filteredAverages ? filteredAverages.average_files_per_day : 0,
    growth_rate: filteredGrowthRate ? filteredGrowthRate.growth_rate : 0,
  };
};
