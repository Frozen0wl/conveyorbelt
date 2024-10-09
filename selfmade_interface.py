import cps_gate_python_interface as cps_interface
import cps_gate_constants as cps_constants
import time

cps_gates = {
    '1': cps_interface.Class_CPSGateControl(
        cps_constants.cps01, 
        cps_constants.conveyorbelt_right_flag, 
        cps_constants.conveyorbelt_left_flag, 
        cps_constants.conveyorbelt_stop_flag,
        cps_constants.stopper_down_flag, 
        cps_constants.stopper_up_flag, 
        cps_constants.conveyor_detection_flag
    ),

    

    '2': cps_interface.Class_CPSGateControl(
        cps_constants.cps02, 
        cps_constants.conveyorbelt_right_flag, 
        cps_constants.conveyorbelt_left_flag, 
        cps_constants.conveyorbelt_stop_flag,
        cps_constants.stopper_down_flag, 
        cps_constants.stopper_up_flag, 
        cps_constants.conveyor_detection_flag
    ),


        '3': cps_interface.Class_CPSGateControl(
        cps_constants.cps03, 
        cps_constants.conveyorbelt_right_flag, 
        cps_constants.conveyorbelt_left_flag, 
        cps_constants.conveyorbelt_stop_flag,
        cps_constants.stopper_down_flag, 
        cps_constants.stopper_up_flag, 
        cps_constants.conveyor_detection_flag
    ),

        '4': cps_interface.Class_CPSGateControl(
        cps_constants.cps04, 
        cps_constants.conveyorbelt_right_flag, 
        cps_constants.conveyorbelt_left_flag, 
        cps_constants.conveyorbelt_stop_flag,
        cps_constants.stopper_down_flag, 
        cps_constants.stopper_up_flag, 
        cps_constants.conveyor_detection_flag
    ),

        '5': cps_interface.Class_CPSGateControl(
        cps_constants.cps05, 
        cps_constants.conveyorbelt_right_flag, 
        cps_constants.conveyorbelt_left_flag, 
        cps_constants.conveyorbelt_stop_flag,
        cps_constants.stopper_down_flag, 
        cps_constants.stopper_up_flag, 
        cps_constants.conveyor_detection_flag
    ),

        '6': cps_interface.Class_CPSGateControl(
        cps_constants.cps06, 
        cps_constants.conveyorbelt_right_flag, 
        cps_constants.conveyorbelt_left_flag, 
        cps_constants.conveyorbelt_stop_flag,
        cps_constants.stopper_down_flag, 
        cps_constants.stopper_up_flag, 
        cps_constants.conveyor_detection_flag
    ),
}

def run(gate: int):
    cps_gates[str(gate)].run_conveyorbelt_right()

def stop(gate: int):
    cps_gates[str(gate)].stop_conveyorbelt()

def stop_all():
    for gate in cps_gates.values():
        gate.stop_conveyorbelt()

def run_all():
    for gate in cps_gates.values():
        gate.run_conveyorbelt_right()

def block(gate: int):
    cps_gates[str(gate)].move_stopper_up()
    
def unblock(gate: int):
    cps_gates[str(gate)].move_stopper_down()
    
def block_all():
    for gate in cps_gates.values():
        gate.move_stopper_up()
        
def unblock_all():
    for gate in cps_gates.values():
        gate.move_stopper_down()

def detect(gate: int):
    return cps_gates[str(gate)].conveyor_detection_state()

def test(gate: int):
    print("Testing gate", gate)
    while(not detect(gate)):
        continue
    print("Detected")
    stop(gate)

