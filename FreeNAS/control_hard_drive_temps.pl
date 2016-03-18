#!/usr/bin/perl

# This script works on SuperMicro X9 and X10 motherboards to control case
# fan speed mode in response to hard drive temperatures.
# It should be set as a cron job to run on roughly a five minute interval.

# set fan speed to 50% duty cycle (max is 64)
# ipmitool raw 0x30 0x70 0x66 0x01 0x00 0x32

# edit the following values
$number_of_hard_drives = 5;
$hd_designator = "/dev/da";

# edit nothing below this line

$max_temp = 0;

foreach $item (0..$number_of_hard_drives-1) {
  $command = "/usr/local/sbin/smartctl -A $hd_designator$item | grep Temp";

  # print "$command\n";

  $output = `$command`;
  @vals = split(" ", $output);

  # grab last item from the output, which is the hard drive temperature
  $temp = "$vals[-1]\n";

  # update maximum drive temperature
  $max_temp = $temp if $temp > $max_temp;
}

if ($max_temp > 39) {
  # at least one hard drive is 40 deg C or higher
  # set fan speed control to Full
  `ipmitool raw 0x30 0x45 0x01 0x01`
} 

elsif ($max_temp == 39 ){
  # maximum drive temperature is 39 deg C
  # set fan speed to Standard
  `ipmitool raw 0x30 0x45 0x01 0x00`
}
  
else {
  # all hard drive temperatures are 38 deg C or cooler
  # set fan speed control to Optimal
  `ipmitool raw 0x30 0x45 0x01 0x02`
}
