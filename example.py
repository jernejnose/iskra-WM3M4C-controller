from wm3m4c import *
import time

# initialise and connect to meter
meter = WM3M4C(33)
meter.connect("/dev/ttyUSB0")

#  set meter time
meter.set_time(time.time())

# set signing profile
meter.set_signing_profile(sig_format="hex")

# create and upload billing dataset
billing_dataset = build_billing_dataset(CT="controller1")
meter.set_billing_dataset(billing_dataset)

# if meter is idle start new measurement
if meter.get_measurement_status() == 0:
    meter.start_measurement()

# wait some time
time.sleep(10)

# stop measurement
meter.stop_measurement()

# wait for meter to sign measurement (it takes around 1 s)
time.sleep(1.5)

# print out billing dataset, signature and public key
print("signature status: ", meter.get_signature_status())
print("billing data: ", meter.get_output_billing_dataset())
print("signature: ", meter.get_signature())
print("public key: ", meter.get_public_key())
