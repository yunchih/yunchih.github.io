# Research

{{< figure
  src="/img/profile.jpg" alt="Yun-Chih" class="left profile"
>}}

My research focuses on operating systems, file systems, databases, and computer architecture. If you enjoy building real-world systems and infrastructure, this could be a great opportunity for you! I have extensive experience with open-source system projects. I also have strong collaborations with researchers in Germany. We have opportunities for international research exchange!

Before joining NTHU, I was a postdoc at Technische Universität Dortmund in Germany. My recent research explores hardware-software co-design to reduce the carbon footprint of computing.

I am looking for students who are passionate about building system. If you’re interested, feel free to reach out! Let’s build something exciting together! 

我們的研究團隊正在尋找對系統研究充滿熱情的學生！無論你想找碩班、博班指導老師、大學專題研究，都歡迎寄信給我，一起聊聊。

![email](img/email.png)


# 研究方向

電腦越來越快、越來越便宜，但進步的背後，如何永續？
本實驗室致力於研究軟硬體整合的系統架構，降低數位基礎設施的碳足跡，同時確保長期可靠性與運算永續性。

根據美國能源部（DOE）與國際能源總署（IEA）最新報告，**2028 年資料中心耗電將佔全美總電力的 6.7–12%**，其中**冷卻能耗高達 75%**。在高效能伺服器中，**DRAM 佔整體功耗的 30–50%**；即使採用 ECC 防護與液冷技術，記憶體仍因高溫導致資料保持時間急遽下降，僅刷新命令就消耗了**約 35% 的 DRAM 能量與 25% 的頻寬**。這些能耗並未轉化為實質計算，而是浪費於維持「可靠度幻覺」的代價。

更令人憂心的是，**快閃記憶體的碳足跡已超過高階 CPU 十倍**。伺服器中的 SSD 平均僅使用設計壽命的 **15%** 即退役，手機的快閃記憶體則往往只使用不到 **5%** 就與整機一同報廢。2023 年台灣僅有 **12% 舊手機被回收**；即便回收，實際減碳效益仍低於製造碳排的 **2%**。換言之，多數儲存裝置在「還未壞、但不再被信任」的情況下提前被丟棄，形成龐大的電子廢棄。

本實驗室的研究結合作業系統、資料結構與計算機架構三大層面，探索如何透過軟硬體整合設計提升系統效能、永續性與耐用度

### 我的專長 (My Expertise)

我是記憶體與儲存系統以及軟硬體整合設計的專家，在電腦架構與系統領域已提出多項重要突破。在 2024 年，我發表的記憶體內搜尋架構（In-Memory Search Architecture）提出將「資料驗證（Data Verification）」邏輯用於「資料索引比對（Data Matching）」，此創新設計有效降低先進製程晶片的能耗與製造碳足跡，榮獲嵌入式系統領域頂級會議 ACM/IEEE CODES+ISSS 最佳論文獎。

我於德國擔任博士後研究員期間，密集參與德國 6GEM 聯盟（預算 4300 萬歐元）、SPP 2377 Priority Program（涵蓋 13 個機構與 23 位主持人），並與慕尼黑工業大學（TU Munich）、卡爾斯魯爾理工學院（Karlsruhe Institute of Technology）等頂尖學府維繫長期合作關係，為臺灣注入豐沛的國際研究動能。我與德國合作團隊於 ICDE 2025 發表論文，將記憶體可靠性（Memory Reliability）視為可調維度，設計可在錯誤中運作的 Error-Adaptive Data Structures。此概念挑戰資料庫系統長期以來的「完美記憶體」假設，使儲存與資料庫系統能在可靠度、能耗與成本之間取得新平衡。

我長期深耕低功耗系統設計，兩度獲得 ISLPED 最佳論文獎提名（2021, 2023），並發表多樣成果於 IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems，與 DAC、ICCAD 等頂尖會議發表九篇論文，並於 2024 年受邀在 ESWEEK 會議開設 Tutorial，同時擔任 IEEE CASES 與 ICCD Program Committee，以及 ESWEEK 2025 籌備委員。
我的博士論文提出「資料生命週期導向的垂直整合設計（Vertical Integration for Lifetime-Aware Storage Systems）」，降低錯誤修正開銷並延長快閃記憶體壽命。此貢獻使我榮獲台灣資訊儲存技術協會博士論文獎與劉炯朗教授博士獎學金。

# Teaching

[Operating System (2025 Fall)](https://sys-nthu.github.io/os25-fall/): many material for you to explore!

# My Background 

- **2024/01 - 2025/06**: Postdoctoral Researcher, TU Dortmund, Germany
- **2023/08 - 2023/12**: Postdoctoral Researcher, Academia Sinica, Taiwan
- **2018/08 - 2023/07**: Ph.D. in Computer Science \& Information Engineeering, National Taiwan University (Advisor: Prof. Tei-Wei Kuo)
- **2014 - 2018**: B.S. in Computer Science \& Information Engineering, National Taiwan University

# Services

- **2025**: Technical Program Committee Member (IEEE International Conference on Computer Design (ICCD))
- **2025**: Technical Program Committee Member (International Conference on Compilers, Architecture, and Synthesis for Embedded Systems (CASES))
- **2025**: Web Chair (Embedded Systems Week)

# Awards

- **2024**: Best Paper Award (2024 CODES+ISSS conference)
- **2023**: Taiwan Information Storage Association PhD Dissertation Award
- **2021**: Synopsys - Prof. Chung Laung Liu Ph.D. Fellowship

# Publications

- {{< publication
    authors="Maximilian Berens, Yun-Chih Chen, Jian-Jia Chen, Jens Teubner"
    title="Beyond Bandwidth Doubling: Embrace Bit-Flips & Unlock Processing-in-NAND"
    conference="Proceedings of the IEEE International Conference on Data Engineering (ICDE)"
    year="2025" >}}
- {{< publication
    authors="Yun-Chih Chen, Yuan-Hao Chang, Tei-Wei Kuo"
    title="Reliable, Versatile, and Efficient Data Matching in SSD's NAND Flash Memory Chip for Data Indexing Acceleration"
    conference="IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (Integrated with ACM/IEEE CODES+ISSS'24) **(Best Paper Award) (1 out of 198 papers)**"
    year="2024" >}}
- {{< publication
    authors="Wen-Yi Wang, Chun-Feng Wu, Yun-Chih Chen, Tei-Wei Kuo, Yuan-Hao Chang"
    title="GEAR: Graph-Evolving Aware Data ArrangeR to Accelerate Traversing Evolving Graphs on SCM"
    conference="IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (Integrated with ACM/IEEE CODES+ISSS'24)"
    year="2024" >}}
- {{< publication
    authors="Chun-Lin Chu, Yun-Chih Chen, Wei Cheng, Ing-Chao Lin, Yuan-Hao Chang"
    title="AttentionRC: A Novel Approach to Improve Locality Sensitive Hashing Attention on Dual-addressing Memory"
    conference="IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (Integrated with ACM/IEEE CODES+ISSS'24)"
    year="2024" >}}
- {{< publication
    authors="Lin, Shi-Zhe, Yun-Chih Chen, Yuan-Hao Chang, Tei-Wei Kuo"
    title="LUTIN: Efficient Neural Network Inference with Table Lookup"
    conference="IEEE/ACM International Symposium on Low Power Electronics and Design (ISLPED)"
    year="2024" >}}
- {{< publication
    authors="Yun-Chih Chen, Yuan-Hao Chang, Tei-Wei Kuo"
    title="Search-in-Memory (SiM): Conducting Data-Bound Computations on Flash Chip for Enhanced Efficiency"
    conference="Design, Automation & Test in Europe Conference & Exhibition (DATE)"
    year="2024" >}}
- {{< publication
    authors="Hsu, Tsung-Yen, Chen, Yi-Shen, Yun-Chih Chen, Yuan-Hao Chang, Tei-Wei Kuo"
    title="REFORM: Responsive, Energy-efficient Frame Rendering for Mobile Devices"
    conference="IEEE/ACM International Symposium on Low Power Electronics and Design (ISLPED) (**Best Paper Award Candidate**)"
    year="2023" >}}
- {{< publication
    authors="Wu, Zheng-Wei, Yun-Chih Chen, Yuan-Hao Chang, Tei-Wei Kuo"
    title="APP: Enabling Soft Real-Time Execution on Densely-Populated Hybrid Memory System"
    conference="60th ACM/IEEE Design Automation Conference (DAC)"
    year="2023" >}}
- {{< publication
    authors="Lo, Chih-Ting, Yun-Chih Chen, Yuan-Hao Chang, Tei-Wei Kuo"
    title="HAPIC: a Scalable, Lightweight and Reactive Cache for Persistent-Memory-based Index"
    conference="ACM/IEEE International Conference on Computer-Aided Design (ICCAD)"
    year="2023" >}}
- {{< publication
    authors="Yun-Chih Chen, Wu, Chun-Feng, Yuan-Hao Chang, Tei-Wei Kuo"
    title="ZoneLife: How to Utilize Data Lifetime Semantics to Make SSDs Smarter"
    conference="IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems"
    year="2023" >}}
- {{< publication
    authors="Alhasan, Hasan, Yun-Chih Chen, Ho, Chien-Chung, Tei-Wei Kuo"
    title="RUSM: Harnessing Unused Resources in 3D NAND SSD to Enhance Reading Performance"
    conference="IEEE 11th Non-Volatile Memory Systems and Applications Symposium (NVMSA)"
    year="2022" >}}
- {{< publication
    authors="Yun-Chih Chen, Wu, Chun-Feng, Yuan-Hao Chang, Tei-Wei Kuo"
    title="Reptail: Cutting Storage Tail Latency with Inherent Redundancy"
    conference="58th ACM/IEEE Design Automation Conference (DAC)"
    year="2021" >}}
- {{< publication
    authors="Alhasan, Hasan, Yun-Chih Chen, Ho, Chien-Chung"
    title="RVO: Unleashing SSD’s Parallelism by Harnessing the Unused Power"
    conference="IEEE/ACM International Symposium on Low Power Electronics and Design (ISLPED) (**Best Paper Award Candidate**)"
    year="2021" >}}
