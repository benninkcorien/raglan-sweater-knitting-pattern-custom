# raglan-sweater-knitting-pattern-custom
A python script that generates a raglan sweater based on your measurements and gauge

## Enter measurements

Enter your measurements in cm here:

        measurements = {
            "stitch_gauge": 12.5,
            "row_gauge": 16.0,
            "10cmknitishowmuchyarn": 42.0,
            "metersperballofyarn": 70.0,
            "chestcircumf": 95.0,
            "sleevelength": 52.0,
            "cuff": 21.0,
            "upperarm": 32.0,
            "crewneck": 47.0,
            "bodylength": 52.0,
            "raglanlength": 16.5,
            "waist": 82.0,
            "chesttowaist": 24.0,
            "hip": 96.0,
        }
Or comment that out and use the inputs

## How much yarn is needed

Knit 10 cm, unravel and measure in cm how much yarn you used to do that. This is used to calculate the total needed.
(Tested for accuracy with 1 sweater. This script returns slightly more than used.)
