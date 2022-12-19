100x100_Normal_Data_Sample (6.7.19) - This data is normal signal data and merged with faulty data as described below...

'Max' & 'Mean' features were extracted from both normal and faulty data signals to make processing faster.

Training-Data:
First -> 60 Rows -> of Faulty Data Samples -> Label 0
First -> 60 Rows -> of Normal Data Samples -> Label 1
Merge both together = 120 Rows

Testing-Data:
Last -> 40 Rows -> of Faulty Data Samples -> Label 0
Last -> 40 Rows -> of Normal Data Samples -> Label 1
Merge both together = 80 Rows


First Drift-Fault genereation: Normal Signal + 0.5
Second Drift-Fault genereation: Normal Signal + 0.1

0.01_Change_Drift_Fault_Samples\0.01_