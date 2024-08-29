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
```

## Circuit Diagram
```mermaid
flowchart
    subgraph RaspberryPi
        stepPin --- GPIO22 --- 15
        dircPin --- GPIO17 --- 11
        GND-R --- 9
        3.3VPWR --- 17
    end
    subgraph A4988
        15 --- STEP
        11 --- DIRECTION
        9 --- GND-A
        17 --- VDD
        SLEEP --- RESET
        VMOT
        GND-E
        1A
        1B
        2A
        2B
    end
    subgraph Motor
        1A --- M1
        1B --- M2
        2A --- M3
        2B --- M4
    end

    VMOT --- 9V+
    GND-E --- 9V-
    9V --- 9V+
    9V --- 9V-
    9V+ --- 47μF
    47μF --- 9V-
```

## 参考
https://pongsuke.hatenablog.com/entry/2019/08/08/172359
https://dev.classmethod.jp/articles/raspberrypi-opencv-monitoring/
