# FILE NAME - firewall_traffic_analyzer.py

# NAME: Gabriel Huertas
# DATE: 10/14/25
# BRIEF DESCRIPTION:  This program analyzes network traffic based on port number and data transfer size to assess potential security risk.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
print("=== Network Traffic Security Analyzer ===\n")


port_number = int(input("Enter the port number (e.g., 80, 22, 443, 3389): "))
transfer_size = int(input("Enter the data transfer size in megabytes (MB): "))

print("\nFIREWALL LOG:")
print(f"Port: {port_number}, Transfer Size: {transfer_size} MB")


if (port_number == 22 or port_number == 3389) and transfer_size > 500:
    print("Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!")
elif (port_number == 80 or port_number == 8080) and transfer_size > 100:
    print("Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.")
elif port_number == 443 or port_number == 8443:
    print("Risk Assessment: LOW RISK: Secure encrypted transfer detected.")
else:
    print("Risk Assessment: UNKNOWN: Unrecognized traffic pattern.")

print("------------------------")



########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 80
Enter the data transfer size in megabytes (MB): 120

FIREWALL LOG:
Port: 80, Transfer Size: 120 MB
Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 22
Enter the data transfer size in megabytes (MB): 1200

FIREWALL LOG:
Port: 22, Transfer Size: 1200 MB
Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 443
Enter the data transfer size in megabytes (MB): 1024

FIREWALL LOG:
Port: 443, Transfer Size: 1024 MB
Risk Assessment: LOW RISK: Secure encrypted transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 1725
Enter the data transfer size in megabytes (MB): 234567

FIREWALL LOG:
Port: 1725, Transfer Size: 234567 MB
Risk Assessment: UNKNOWN: Unrecognized traffic pattern.
------------------------
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Did you get tripped up using the `or` or `and` operators? If so, how?

a little bit because I forgot both side of 'or' need their own comparison





'''
