#! /opt/local/bin/zsh

#cd /Users/kwh/sw_projects/git/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports;
#grep Scotia /Users/kwh/sw_projects/git/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv | perl -e -a -F"," 'print "$F[-1]"'

cd /Users/kwh/sw_projects/git/COVID-19
git pull

for prov in "Province" "British Columbia" "Ontario" "Quebec" "New Brunswick" "Prince Edward Island" "Nova Scotia"; 
#   do echo -n "$prov "; grep $prov /Users/kwh/sw_projects/git/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv | awk -F "," '{print $NF}';
  do grep $prov /Users/kwh/sw_projects/git/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv | awk -F "," '{ printf "%22s %8s \n", $1, $NF}';
done

cd /Users/kwh/sw_projects/git/covid-19-data
git pull

for county in "Grant,Wa" "Walla" "Yakima" "Clatsop" "Brown,W" "Manitowoc";
  do grep $county /Users/kwh/sw_projects/git/covid-19-data/us-counties.csv | tail -n -1 | awk -F "," '{ printf "%12s %12s %5s \n", $1, $2, $(NF-1) }'
done
