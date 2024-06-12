from wm3m4c import *
import time
import binascii

# initialise and connect to meter
meter = WM3M4C(33)
meter.connect("COM5")

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
print("signature: ", binascii.hexlify(meter.get_signature()).decode('utf-8'))
print("public key: ", binascii.hexlify(meter.get_public_key()).decode('utf-8'))
