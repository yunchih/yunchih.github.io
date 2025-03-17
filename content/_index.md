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

- **2024**: Best Paper Award (2024 CODES+ISSS conference)
- **2023**: Taiwan Information Storage Association PhD Dissertation Award
- **2021**: Synopsys - Prof. Chung Laung Liu Ph.D. Fellowship
- **2019**: Excellent TA Award (CSIE2311 - Network Admin. & System Admin.)
- **2018**: Excellent TA Award (CSIE2311 - Network Admin. & System Admin.)
