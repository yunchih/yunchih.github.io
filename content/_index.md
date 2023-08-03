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
personal_title: "PhD Student"
# An address (you can list multiple)
address: 
  - 
    name: National Taiwan University
    street: Room 438, Dept. of Computer Science & Engineering, No.1, Sec. 4, Roosevelt Road
    postal_code: 10617
    locality: Taipei, Taiwan

# === Optional fields ===
# Add an email with a mailto: hyperlink
# email: aaaa@example.com
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
        - name: Yuan-Hao Chang
        - name: and Tei-Wei Kuo
    title: "Optimized Ephemeral Data Storage"
    # Will write "In ${journal}, ${date}"
    date: 2022
    journal: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
    citation: "@ARTICLE{9964402,\n
  author={Chen, Yun-Chih and Wu, Chun-Feng and Chang, Yuan-Hao and Kuo, Tei-Wei},\n
  journal={IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems}, \n
  title={ZoneLife: How to Utilize Data Lifetime Semantics to Make SSDs Smarter}, \n
  year={2022},\n
  volume={},\n
  number={},\n
  pages={1-1},\n
  doi={10.1109/TCAD.2022.3224898}}"

    pdf: https://ieeexplore.ieee.org/document/9964402
    # A list of link that will appear as badges at the bottom of the publication.
    links:
      -
        name: Two page abstract
        url: "https://yunchih.thycat.com/files/DAC2023-PhD-Forum-Abstract-Yun-Chih-Chen-v1.pdf"
      -
        name: Poster
        url: "https://yunchih.thycat.com/files/DAC2023-PhD-Forum-Poster-Yun-Chih-Chen-v1.pdf"
    # A description for the paper.
    description: I propose a novel multi-ECC SSD firmware to store short-lived data with significantly less resources yet strong guarantee on data safety.  Experiments show enhanced throughput and expanded endurance.
  - 
    authors:
        - name: Hasan Alhasan
        - name: Yun-Chih Chen
          me: true
        - name: and Chien-Chung Ho
    title: "SSD Power Efficiency Enhancement"
    # Will write "In ${journal}, ${date}"
    date: 2020
    journal: IEEE/ACM International Symposium on Low Power Electronics and Design (ISLPED)
    citation: "@INPROCEEDINGS{9502496,\n
  author={Alhasan, Hasan and Chen, Yun-Chih and Ho, Chien-Chung},\n
  booktitle={2021 IEEE/ACM International Symposium on Low Power Electronics and Design (ISLPED)},\n
  title={RVO: Unleashing SSD’s Parallelism by Harnessing the Unused Power},\n
  year={2021},\n
  pages={1-6},\n
  doi={10.1109/ISLPED52811.2021.9502496}}"

    pdf: https://ieeexplore.ieee.org/document/9502496
    description: I identified energy under-utilization in conventional NAND flash programming and proposed a low-level command that recycles the wastage to enhance system parallelism.  Accompanied by a scheduling framework, my design achieves industrial-grade read latency requirements, even in write-intensive workloads.
  - 
    authors:
        - name: Yun-Chih Chen
          me: true
        - name: Chun-Feng Wu
        - name: Yuan-Hao Chang
        - name: and Tei-Wei Kuo
    title: "Performant Consistent Storage Design"
    # Will write "In ${journal}, ${date}"
    date: 2021
    journal: ACM/IEEE Design Automation Conference (DAC)
    citation: "@INPROCEEDINGS{9586218,\n
  author={Chen, Yun-Chih and Wu, Chun-Feng and Chang, Yuan-Hao and Kuo, Tei-Wei},\n
  booktitle={2021 58th ACM/IEEE Design Automation Conference (DAC)}, \n
  title={Reptail: Cutting Storage Tail Latency with Inherent Redundancy},\n 
  year={2021},\n
  volume={},\n
  number={},\n
  pages={595-600},\n
  doi={10.1109/DAC18074.2021.9586218}}"

    pdf: https://ieeexplore.ieee.org/document/9586218
    description: I proposed a hardware-software co-design that exploits the inherent redundancy in journaling file-system to improves the 99th percentile read latency of ultra-dense SSD by 40%.  My design overcomes several technical challenges, such as journal fragmentation, space limitation and communication of semantics.


---
# Bio

My research focuses on hardware/software co-design for Solid State Drives (SSDs). I’m currently working on the design of peripheral circuits within NAND flash chips that can perform bulk bitwise processing in-memory. The novel circuit will enable database indexes to take advantage of SSD’s massive parallelism and beyond-DRAM capacity.
