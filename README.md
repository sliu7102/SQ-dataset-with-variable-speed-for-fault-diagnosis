# SQ speed variation vibration signal data set

Here, we expose a variable speed dataset based on vibration signals to provide a Benchmark Dataset for peer-to-peer measurement of algorithmic model performance to advance the field of research.





## 1. Introduction 

Realizing fault diagnosis under variable speed conditions is not only significant for fault diagnosis of equipment operating under time-varying load and power, but also provides the necessary technical support for realizing full-cycle condition monitoring of equipment including start-up and shutdown phases. In general, order tracking techniques and time-frequency analysis techniques are two commonly used methods to analyze variable speed signals. However, order tracking techniques suffer from distortion due to inaccurate speed extraction and require additional hardware devices to obtain speed-related information. Time-frequency analysis techniques, on the other hand, are highly dependent on manual design and require sufficient a priori knowledge and diagnostic expertise. Therefore, there is a need to conduct research on data-driven intelligent fault diagnosis methods for variable speed conditions to facilitate the development of this research area.

Currently, most of the work on data-driven intelligent diagnosis of mechanical faults is performed under the assumption of constant velocity. This a priori assumption that the training and test data satisfy independent identical distribution brings great convenience to the general intelligent diagnosis algorithms. However, in general, industrial equipment is susceptible to time-varying loads, power, etc., as well as the inevitable acceleration and deceleration processes during the start-stop phase, and the resulting fluctuations in speed often lead to shifts in the distribution of the collected data. In this case, the data used for training as well as testing usually do not satisfy the assumption of independent homogeneous distribution, which places higher demands on intelligent diagnosis, requiring the extraction of valid features from domain-shifted data and generalization to recognition tasks with even unknown distributed domain data. 

Although a lot of researches have been focused on the research fields of variable working conditions and variable speed intelligent diagnosis and have achieved certain results, there is a lack of relevant public variable speed dataset for validation. At the strong request of experts and scholars in the field and journal editors, here we make public a variable speed dataset based on vibration signals, which we hope can become a Benchmark Dataset as a benchmark for the performance of algorithm models among peers, which is very lacking and necessary for the field of mechanical fault diagnosis, especially for variable speed working conditions.



## 2. Equipments Description

The experiment utilized a comprehensive mechanical failure simulation test stand from SQ (Spectra Quest) for the motor bearing outer and inner ring failure simulation.



The structure of the test bench is shown in Figure 1, the test bench consists of three major parts: motor, rotor and load, the experiment uses piezoelectric acceleration sensor to collect the motor bearing signal, the data acquisition instrument used is CoCo80, the sampling frequency is 25.6 KHz. motor bearing model NSK6203, the fault bearing is located in the motor drive end, the acceleration sensor is deployed in the motor drive end cover through the magnet base The acceleration sensor is deployed on the end cover of the motor drive end via a magnet base directly above.



![Fig. 1. SQV test rig](https://github.com/sliu7102/SQ-dataset-with-variable-speed-for-fault-diagnosis/blob/main/ReadMe/SQV%20test%20rig.png 'Fig. 1. SQV test rig')

In this simulation experiment, we simulated a total of six faults, including inner-ring faults (IF) and outer-ring faults (OF) at three different damage levels, respectively. As shown in Figure 2, we quantified the degree of fault damage by machining artificially created single-point defects with different damage diameters and depths, as shown in Table 1. The quantitative results are verified on the bearing failure degree analysis algorithm based on the second generation wavelet packet analysis and the shock pulse method.















