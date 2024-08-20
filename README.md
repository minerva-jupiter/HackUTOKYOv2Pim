# HackUTOKYOv2Pim

## system design
```mermaid
stateDiagram-v2
    [*] --> UnlockHandle
    
    UnlockHandle --> Wait

    Wait --> EscapeLeft :RightSensor
    EscapeLeft --> Wait :0.2sec

    Wait --> EscapeRight :LeftSensor
    EscapeRight --> Wait :0.2sec
    Wait --> Confusion :TakenOffHandle
    state Confusion {
        Roll --> Erupt
    }
    Confusion --> [*] :10sec
```