<<<<<<< HEAD
---
# === Required fields  ===
# Your name 
name: "Yun-Chih Chen"
# Your profile picture
imgname: 
  name: "img/profile.jpg"
  alt: "Yun-Chih Chen"
  type: image/jpeg
# More sources can be added (optional) using 
# imgOther:
#   - name: $IMAGE_PATH
#     type: $IMAGE_TYPE
#   - name: $IMAGE_PATH
#     type: $IMAGE_TYPE
# ...
# A title (job title or "Researcher", "PhD student", etc.)
personal_title: "Postdoctoral Researcher"
# An address (you can list multiple)
address: 
  - 
    name: Technical University of Dortmund
    street: Otto-Hahn-Strasse 16
    postal_code: 44227
    locality: Dortmund, Germany

# === Optional fields ===
# Add an email with a mailto: hyperlink
email: yunchih.chen@tu-dortmund.de
# Add an email "image" for spam protection. With light and dark mode
# emailImg: 
#   dark: /img/dark_email.png
#   light: /img/light_email.png

# List your publications. The required fields are pdf, title, and image 
# (which should be the image path). The other fields are optional.
publications:
  - 
    authors:
        - name: Yun-Chih Chen
          me: true
        - name: Chun-Feng Wu
        - name: Yuan-Hao Chang,
        - name: Tei-Wei Kuo
    title: "Reliable, Versatile, and Efficient Data Matching in SSD's NAND Flash Memory Chip for Data Indexing Acceleration"
    date: 2024
    journal: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD). (Integrated with ACM/IEEE CODES+ISSS'24) (**Best Paper Award**)
  - 
    authors:
        - name: Wen-Yi Wang
        - name: Chun-Feng Wu
        - name: Yun-Chih Chen
          me: true
        - name: Tei-Wei Kuo,
        - name: Yuan-Hao Chang
    title: "GEAR: Graph-Evolving Aware Data ArrangeR to Enhance the Performance of Traversing Evolving Graphs on SCM"
    date: 2024
    journal: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD). (Integrated with ACM/IEEE CODES+ISSS'24)
  - 
    authors:
        - name: Shi-Zhe Lin
        - name: Yun-Chih Chen
          me: true
        - name: Yuan-Hao Chang
        - name: Tei-Wei Kuo,
        - name: Hsiang-Pang Li
    title: "LUTIN: Efficient Neural Network Inference with Table Lookup"
    date: 2024
    journal: IEEE/ACM International Symposium on Low Power Electronics and Design (ISLPED)
  - 
    authors:
        - name: Chih-Ting Lo
        - name: Yun-Chih Chen
          me: true
        - name: Yuan-Hao Chang,
        - name: Tei-Wei Kuo
    title: "HAPIC: A Scalable, Lightweight and Reactive Cache for Persistent-Memory-Based Index"
    date: 2023
    journal: IEEE/ACM International Conference on Computer Aided Design (ICCAD)
  - 
    authors:
        - name: Zheng-Wei Wu
        - name: Yun-Chih Chen
          me: true
        - name: Yuan-Hao Chang,
        - name: Tei-Wei Kuo
    title: "APP: Enabling Soft Real-Time Execution on Densely-Populated Hybrid Memory System"
    date: 2023
    journal: ACM/IEEE Design Automation Conference (DAC)
  - 
    authors:
        - name: Tsung-Yen Hsu
        - name: Yi-Shen Chen
        - name: Yun-Chih Chen
          me: true
        - name: Yuan-Hao Chang,
        - name: Tei-Wei Kuo
    title: "REFORM: Responsive, Energy-efficient Frame Rendering for Mobile Devices"
    date: 2023
    bestpaper: yes
    journal: IEEE/ACM International Symposium on Low Power Electronics and Design (ISLPED)
  - 
    authors:
        - name: Yun-Chih Chen
          me: true
        - name: Chun-Feng Wu
        - name: Yuan-Hao Chang,
        - name: Tei-Wei Kuo
    title: "ZoneLife: How to Utilize Data Lifetime Semantics to Make SSDs Smarter"
    date: 2022
    journal: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
  - 
    authors:
        - name: Hasan Alhasan
        - name: Yun-Chih Chen
          me: true
        - name: Chien-Chung Ho,
        - name: Tei-Wei Kuo
    title: "RUSM: Harnessing Unused Resources in 3D NAND SSD to Enhance Reading Performance"
    date: 2022
    journal: IEEE Non-Volatile Memory Systems and Applications Symposium (NVMSA)
  - 
    authors:
        - name: Yun-Chih Chen
          me: true
        - name: Chun-Feng Wu
        - name: Yuan-Hao Chang,
        - name: Tei-Wei Kuo
    title: "Reptail: Cutting Storage Tail Latency with Inherent Redundancy"
    date: 2021
    journal: ACM/IEEE Design Automation Conference (DAC)
  - 
    authors:
        - name: Hasan Alhasan
        - name: Yun-Chih Chen
          me: true
        - name: Chien-Chung Ho
    title: "RVO: Unleashing SSD’s Parallelism by Harnessing the Unused Power"
    date: 2021
    bestpaper: yes
    journal: IEEE/ACM International Symposium on Low Power Electronics and Design (ISLPED)


---
# Research

I received PhD degree in 2023 from National Taiwan University, Computer Science \& Information Engineering, supervised by Prof. Tei-Wei Kuo.
My PhD dissertation introduced vertical integration solutions for storage systems that leveraged application semantics to optimize hardware request scheduling and reduce error correction costs.
Another key contribution of my dissertation was a processing-in-memory chip with an emphasis on real-world applicability. Instead of adding a dedicated processor, I re-purposed existing logic in memory chips for highly parallel data matching while preserving their traditional roles in read-out and memory management. The result was a cost-effective, versatile chip that significantly reduced the database system’s dependency on power-hungry DRAM-based caches. This work won the **Best Paper Award in 2024 CODES+ISSS conference (1 out of 198 papers)**.

My ongoing research focuses on designing sustainable and fault-tolerant memory systems to tackle the declining reliability issue in modern memory technologies. 
In the long term, I aim to design modular and flexible architectural support for heterogeneous, highly-integrated SoCs.  This support will enable efficient execution of different computation phases in a data pipeline across diverse accelerators while providing an abstraction layer to manage the unique properties of various memory media.




# Teaching

- Teaching Assistant: From 2015 to 2019, I worked as a teaching assistant in the NTU CS's Public Workstation Laboratory.  I led a 17-person system team responsible for the department's public computing services.    For three semesters, I delivered lectures and created course materials for a 72-student class. I also mentored undergraduate interns.
- I mentored numerous undergrad students, nine master students, and four PhD student throughout my PhD study and post-doctoral position.
- I teach a 4-hour course, Real-time Operating System, in TU Dortmund in winter semester, 2024


# Awards:
=======
# Research

{{< figure
  src="/img/profile.jpg" alt="Yun-Chih" class="left profile"
>}}

I am currently a postdoctoral researcher at TU Dortmund, Germany. I will join National Tsing Hua University as an assistant professor in August, 2025.

My research focuses on operating systems, file systems, databases, and computer architecture. If you enjoy building real-world systems and infrastructure, this could be a great opportunity for you! I have extensive experience with open-source system projects.  I also have strong collaborations with researchers in Germany.  We have opportunities for international research exchange.

I am always looking for motivated students who are passionate about system research.  If you’re interested, feel free to reach out! Let’s build something exciting together!

我們的研究團隊正在尋找對系統研究充滿熱情的學生！無論你想找碩班、博班指導老師、大學專題研究，都歡迎寄信給我，一起聊聊。

我跟德國的研究團隊保持緊密合作，提供國際交換的機會。

![email](img/email.gif)

# My Background 

- **2024 - present**: Postdoctoral Researcher, TU Dortmund, Germany
- **2023/08 - 2023/12**: Postdoctoral Researcher, TU Dortmund, Germany
- **2018 - 2023/07**: Ph.D. in Computer Science \& Information Engineeering, National Taiwan University (Advisor: Prof. Tei-Wei Kuo)
- **2014 - 2018**: B.S. in Computer Science \& Information Engineering, National Taiwan University

# Services

- **2025**: Technical Program Committee Member (International Conference on Compilers, Architecture, and Synthesis for Embedded Systems (CASES))
- **2025**: Web Chair (ESWEEK)

# Awards
>>>>>>> nthu

- **2024**: Best Paper Award (2024 CODES+ISSS conference)
- **2023**: Taiwan Information Storage Association PhD Dissertation Award
- **2021**: Synopsys - Prof. Chung Laung Liu Ph.D. Fellowship
<<<<<<< HEAD
- **2019**: Excellent TA Award (CSIE2311 - Network Admin. & System Admin.)
- **2018**: Excellent TA Award (CSIE2311 - Network Admin. & System Admin.)
=======

# Publications

- {{< publication
    authors="Maximilian Berens, Yun-Chih Chen, Jian-Jia Chen, Jens Teubner"
    title="Beyond Bandwidth Doubling: Embrace Bit-Flips & Unlock Processing-in-NAND"
    conference="Proceedings of the IEEE International Conference on Data Engineering (ICDE)"
    year="2025" >}}
- {{< publication
    authors="Yun-Chih Chen, Yuan-Hao Chang, Kuo, Tei-Wei"
    title="Reliable, Versatile, and Efficient Data Matching in SSD's NAND Flash Memory Chip for Data Indexing Acceleration"
    conference="IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (Integrated with ACM/IEEE CODES+ISSS'24) **(Best Paper Award) (1 out of 198 papers)**"
    year="2024" >}}
- {{< publication
    authors="Wen-Yi Wang, Chun-Feng Wu, Yun-Chih Chen, Kuo, Tei-Wei, Yuan-Hao Chang"
    title="GEAR: Graph-Evolving Aware Data ArrangeR to Accelerate Traversing Evolving Graphs on SCM"
    conference="IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (Integrated with ACM/IEEE CODES+ISSS'24)"
    year="2024" >}}
- {{< publication
    authors="Chun-Lin Chu, Yun-Chih Chen, Wei Cheng, Ing-Chao Lin,, Yuan-Hao Chang"
    title="AttentionRC: A Novel Approach to Improve Locality Sensitive Hashing Attention on Dual-addressing Memory"
    conference="IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (Integrated with ACM/IEEE CODES+ISSS'24)"
    year="2024" >}}
- {{< publication
    authors="Lin, Shi-Zhe, Yun-Chih Chen, Chang, Yuan-Hao, Kuo, Tei-Wei"
    title="LUTIN: Efficient Neural Network Inference with Table Lookup"
    conference="IEEE/ACM International Symposium on Low Power Electronics and Design (ISLPED)"
    year="2024" >}}
- {{< publication
    authors="Yun-Chih Chen, Chang, Yuan-Hao, Kuo, Tei-Wei"
    title="Search-in-Memory (SiM): Conducting Data-Bound Computations on Flash Chip for Enhanced Efficiency"
    conference="Design, Automation & Test in Europe Conference & Exhibition (DATE)"
    year="2024" >}}
- {{< publication
    authors="Hsu, Tsung-Yen, Chen, Yi-Shen, Yun-Chih Chen, Chang, Yuan-Hao, Kuo, Tei-Wei"
    title="REFORM: Responsive, Energy-efficient Frame Rendering for Mobile Devices"
    conference="IEEE/ACM International Symposium on Low Power Electronics and Design (ISLPED) (**Best Paper Award Candidate**)"
    year="2023" >}}
- {{< publication
    authors="Wu, Zheng-Wei, Yun-Chih Chen, Chang, Yuan-Hao, Kuo, Tei-Wei"
    title="APP: Enabling Soft Real-Time Execution on Densely-Populated Hybrid Memory System"
    conference="60th ACM/IEEE Design Automation Conference (DAC)"
    year="2023" >}}
- {{< publication
    authors="Lo, Chih-Ting, Yun-Chih Chen, Chang, Yuan-Hao, Tei-Wei Kuo"
    title="HAPIC: a Scalable, Lightweight and Reactive Cache for Persistent-Memory-based Index"
    conference="ACM/IEEE International Conference on Computer-Aided Design (ICCAD)"
    year="2023" >}}
- {{< publication
    authors="Yun-Chih Chen, Wu, Chun-Feng, Chang, Yuan-Hao, Kuo, Tei-Wei"
    title="ZoneLife: How to Utilize Data Lifetime Semantics to Make SSDs Smarter"
    conference="IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems"
    year="2023" >}}
- {{< publication
    authors="Alhasan, Hasan, Yun-Chih Chen, Ho, Chien-Chung, Kuo, Tei-Wei"
    title="RUSM: Harnessing Unused Resources in 3D NAND SSD to Enhance Reading Performance"
    conference="IEEE 11th Non-Volatile Memory Systems and Applications Symposium (NVMSA)"
    year="2022" >}}
- {{< publication
    authors="Yun-Chih Chen, Wu, Chun-Feng, Chang, Yuan-Hao, Kuo, Tei-Wei"
    title="Reptail: Cutting Storage Tail Latency with Inherent Redundancy"
    conference="58th ACM/IEEE Design Automation Conference (DAC)"
    year="2021" >}}
- {{< publication
    authors="Alhasan, Hasan, Yun-Chih Chen, Ho, Chien-Chung"
    title="RVO: Unleashing SSD’s Parallelism by Harnessing the Unused Power"
    conference="IEEE/ACM International Symposium on Low Power Electronics and Design (ISLPED) (**Best Paper Award Candidate**)"
    year="2021" >}}
>>>>>>> nthu
