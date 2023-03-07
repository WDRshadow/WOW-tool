------- OpenFAST WOW INPUT FILE -------------------------------------------
WOW openFast main config file
---------------------- SIMULATION CONTROL --------------------------------------
True          Echo            - （调试信息）Echo input data to <RootName>.ech (flag)
"FATAL"       AbortLevel      - （信息级别）Error level when simulation should abort (string) {"WARNING", "SEVERE", "FATAL"}
         60   TMax            - （总运行时间）Total run time (s)
     0.0125   DT              - （时间步长）Recommended module time step (s)
          2   InterpOrder     - （插值阶次）Interpolation order for input/output time history (-) {1=linear, 2=quadratic}
          0   NumCrctn        - （修正迭代次数）Number of correction iterations (-) {0=explicit calculation, i.e., no corrections}
      99999   DT_UJac         - （贾可比调用间隔时间）Time between calls to get Jacobians (s)
      1E+06   UJacSclFact     - （贾可比矩阵中使用的比例因子）Scaling factor used in Jacobians (-)
---------------------- FEATURE SWITCHES AND FLAGS ------------------------------
          1   CompElast       - （结构动力学与杆件动力学）Compute structural dynamics (switch) {1=ElastoDyn; 2=ElastoDyn + BeamDyn for blades}
          1   CompInflow      - （入流风）Compute inflow wind velocities (switch) {0=still air; 1=InflowWind; 2=external from OpenFOAM}
          2   CompAero        - （空气动力学）Compute aerodynamic loads (switch) {0=None; 1=AeroDyn v14; 2=AeroDyn v15}
          1   CompServo       - （控制和电气传动）Compute control and electrical-drive dynamics (switch) {0=None; 1=ServoDyn}
          1   CompHydro       - （水动力载荷）Compute hydrodynamic loads (switch) {0=None; 1=HydroDyn}
          0   CompSub         - （支撑结构动力学）Compute sub-structural dynamics (switch) {0=None; 1=SubDyn; 2=External Platform MCKF}
          3   CompMooring     - （系泊系统）Compute mooring system (switch) {0=None; 1=MAP++; 2=FEAMooring; 3=MoorDyn; 4=OrcaFlex}
          0   CompIce         - （冰载荷）Compute ice loads (switch) {0=None; 1=IceFloe; 2=IceDyn}
          0   MHK             - （MHK类型风车）MHK turbine type (switch) {0=Not an MHK turbine; 1=Fixed MHK turbine; 2=Floating MHK turbine}
---------------------- ENVIRONMENTAL CONDITIONS --------------------------------
    9.80665   Gravity         - （重力系数）Gravitational acceleration (m/s^2)
      1.225  AirDens         - （空气密度）Air density (kg/m^3)
       1025   WtrDens         - （水密度）Water density (kg/m^3)
  1.464E-05   KinVisc         - （工作流体粘度）Kinematic viscosity of working fluid (m^2/s)
        335   SpdSound        - （工作流体声速）Speed of sound in working fluid (m/s)
     103500   Patm            - （大气压）Atmospheric pressure (Pa) [used only for an MHK turbine cavitation check]
       1700   Pvap            - （工作流体蒸汽压力）Vapour pressure of working fluid (Pa) [used only for an MHK turbine cavitation check]
        2   WtrDpth         - （水深）Water depth (m)
          0   MSL2SWL         - （静水位和海平面偏移）Offset between still-water level and mean sea level (m) [positive upward]
---------------------- INPUT FILES ---------------------------------------------
"ElastoDyn.dat"    EDFile          - （结构动力学文件）Name of file containing ElastoDyn input parameters (quoted string)
"unused"    BDBldFile(1)    - （杆件动力学文件）Name of file containing BeamDyn input parameters for blade 1 (quoted string)
"unused"    BDBldFile(2)    - （杆件动力学文件）Name of file containing BeamDyn input parameters for blade 2 (quoted string)
"unused"    BDBldFile(3)    - （杆件动力学文件）Name of file containing BeamDyn input parameters for blade 3 (quoted string)
"InflowWind.dat"    InflowFile      - （入流风文件）Name of file containing inflow wind input parameters (quoted string)
"AeroDyn.dat"    AeroFile        - （空气动力学文件）Name of file containing aerodynamic input parameters (quoted string)
"ServoDyn.dat"    ServoFile       - （控制与电气系统文件）Name of file containing control and electrical-drive input parameters (quoted string)
"HydroDyn.dat"    HydroFile       - （水动力载荷文件）Name of file containing hydrodynamic input parameters (quoted string)
"unused"      SubFile         - （支撑结构动力学文件）Name of file containing sub-structural input parameters (quoted string)
"MoorDyn.dat"    MooringFile     - （系泊系统文件）Name of file containing mooring system input parameters (quoted string)
"unused"      IceFile         - （冰载荷文件）Name of file containing ice input parameters (quoted string)
---------------------- OUTPUT --------------------------------------------------
True          SumPrint        - （输出摘要文件）Print summary data to "<RootName>.sum" (flag)
          1   SttsTime        - （屏幕状态信息间隔时间）Amount of time between screen status messages (s)
       1000   ChkptTime       - （重启检查时间）Amount of time between creating checkpoint files for potential restart (s)
     0.0125   DT_Out          - （输出时间步长）Time step for tabular output (s) (or "default")
          0   TStart          - （开始时间）Time to begin tabular output (s)
          0   OutFileFmt      - （输出文件格式）Format for tabular (time-marching) output file (switch) {0: uncompressed binary [<RootName>.outb], 1: text file [<RootName>.out], 2: binary file [<RootName>.outb], 3: both 1 and 2}
True          TabDelim        - （是否使用制表符位分隔符）Use tab delimiters in text tabular output file? (flag) {uses spaces if false}
"ES15.7E2"    OutFmt          - （输出结果格式）Format used for text tabular output, excluding the time channel.  Resulting field should be 10 characters. (quoted string)
---------------------- LINEARIZATION -------------------------------------------
False         Linearize       - （线性化分析）Linearization analysis (flag)
False         CalcSteady      - （是否计算稳态周期工作点）Calculate a steady-state periodic operating point before linearization? [unused if Linearize=False] (flag)
          3   TrimCase        - （要调整的控制参数）Controller parameter to be trimmed {1:yaw; 2:torque; 3:pitch} [used only if CalcSteady=True] (-)
      0.001   TrimTol         - （转速收敛的容差）Tolerance for the rotational speed convergence [used only if CalcSteady=True] (-)
       0.01   TrimGain        - （转速偏差的比例增益）Proportional gain for the rotational speed error (>0) [used only if CalcSteady=True] (rad/(rad/s) for yaw or pitch; Nm/(rad/s) for torque)
          0   Twr_Kdmp        - （塔筒阻尼系数）Damping factor for the tower [used only if CalcSteady=True] (N/(m/s))
          0   Bld_Kdmp        - （叶片阻尼系数）Damping factor for the blades [used only if CalcSteady=True] (N/(m/s))
          2   NLinTimes       - （线性化的次数）Number of times to linearize (-) [>=1] [unused if Linearize=False]
         30,         60    LinTimes        - （线性化时间列表）List of times at which to linearize (s) [1 to NLinTimes] [used only when Linearize=True and CalcSteady=False]
          1   LinInputs       - （输入）Inputs included in linearization (switch) {0=none; 1=standard; 2=all module inputs (debug)} [unused if Linearize=False]
          1   LinOutputs      - （输出）Outputs included in linearization (switch) {0=none; 1=from OutList(s); 2=all module outputs (debug)} [unused if Linearize=False]
False         LinOutJac       - （输出完整加科比行列式）Include full Jacobians in linearization output (for debug) (flag) [unused if Linearize=False; used only if LinInputs=LinOutputs=2]
False         LinOutMod       - （是否需要便携模块级线性化输出文件）Write module-level linearization output files in addition to output for full system? (flag) [unused if Linearize=False]
---------------------- VISUALIZATION ------------------------------------------
          0   WrVTK           - （可视化输出）VTK visualization data output: (switch) {0=none; 1=initialization data only; 2=animation; 3=mode shapes}
          1   VTK_type        - （数据类型）Type of VTK visualization data: (switch) {1=surfaces; 2=basic meshes (lines/points); 3=all meshes (debug)} [unused if WrVTK=0]
false         VTK_fields      - （网格字段）Write mesh fields to VTK data files? (flag) {true/false} [unused if WrVTK=0]
         15   VTK_fps         - （输出帧率）Frame rate for VTK output (frames per second){will use closest integer multiple of DT} [used only if WrVTK=2 or WrVTK=3]
