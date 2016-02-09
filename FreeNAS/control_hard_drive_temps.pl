#!/usr/bin/perl

# edit the following values
$number_of_hard_drives = 5;
$hd_designator = "/dev/da";

# edit nothing below this line

$case = 0;

foreach $item (0..$number_of_hard_drives-1) {
  $command = "/usr/local/sbin/smartctl -A $hd_designator$item | grep Temp";

  # print "$command\n";

  $output = `$command`;
  @vals = split(" ", $output);

  # grab last item from the output, which is the hard drive temperature
  $temp = "$vals[-1]\n";

  # check for temperature greater than 39 deg C
  if ($temp > 39) { $case = 1; }
}

if ($case == 1) {
  # at least one hard drive is 40 deg C or higher
  # set fan speed control to Full
  `ipmitool raw 0x30 0x45 0x01 0x01`
} else {
  # all hard drive temperatures are 39 deg C or cooler
  # set fan speed control to Optimal
  `ipmitool raw 0x30 0x45 0x01 0x02`
}
