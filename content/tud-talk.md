+++
date = "2023-08-03"
title = "My bet on NVM's next ten years"
+++


## The Invisibility of Mature Technology

> "As technology becomes ubiquitous it also becomes invisible." Keven Kelly

As technological innovations mature and become foundational, they seamlessly weave themselves into the fabric of our daily lives.
Keven Kelly's insight guide our exploration of Non-Volatile Memory (NVM)'s next ten years.
In this article, we will explore the multifaceted role of NVM to enable long-term efficiency and continuous learning in the age of AI.  We will talk about the innovative vision of NVM-based storage chips, the future of inference through autonomous agents, and NVM's position under the architecture of future computing system.


## NVM's Role in Modern Systems

The role of Non-Volatile Memory (NVM) extends far beyond traditional data storage. 
No longer should we pursue absolute performance and perceive NVM's relative slowness compared to DRAM as a limitation.  Instead, we should place NVM in a larger context of an integrated System-on-Chip (SoC) where NVM and other components are each strategically leveraged for specific responsibilities based on their specific strength to create a balanced technological ecosystem.

For example, NVM will form the basis for AI's continuous background knowledge discovery and non-intrusive tasks, while leaving real-time tasks to specialized components like Neural Processing Units (NPUs). The division of labor between NVM for background tasks and NPUs for real-time inferences represents a mature approach to system design, optimizing both energy efficiency and responsiveness.

Moreover, as we will explore later, NVM can transcend further beyond its traditional roles. New technology makes it possible to embed computation directly into NVM, leading to our proposal of a novel storage chip with in-chip indexing capability. Unlike general-purpose SSDs that rely on traditional I/O interfaces, this storage chip is designed to be deployed efficiently as a specialized accelerator within a System-on-Chip (SoC). This innovative configuration optimizes both storage and processing, providing a tailored solution that complements the specific demands of modern AI applications.



## The Rise of Large Language Models (LLMs) and Their Connection to NVM

Large Language Models (LLMs) have become a significant area of research and development in artificial intelligence.  Despite their promise, LLMs encounter challenges, especially regarding knowledge limitations, upscaling costs, and model efficiency:

- **Knowledge Bottleneck**: LLMs are restricted to the concepts and facts within their training data, often leading to a knowledge bottleneck.
- **Expensive Scaling**: Incorporating new knowledge requires up-scaling the model size, a process that can be highly resource-intensive.
- **Model Efficiency**: Balancing model size and inference efficiency is a key consideration, particularly for edge computing applications.


### Retrieval-Augmented LLM (RA-LLM)

The Retrieval-Augmented LLM (RA-LLM), a state-of-the-art solution, addresses these challenges by combining a lean LLM with a continually updated data store. This approach enables:

- **Efficient Knowledge Incorporation**: Integration of user activities and new data without extensive retraining.
- **Privacy Preservation**: User data remains secure, without the need for cloud uploads.
- **Edge Deployment Compatibility**: RA-LLM's streamlined design enables efficient edge computing deployment.

### NVM's Role in Supporting RA-LLM

NVM's potential as a storage backend for RA-LLM allows for the continuous ingestion of vector embedding updates, including user-generated content like photos and health data. Moreover, vector retrieval can be expedited through an NVM chip with in-chip indexing capability, highlighting NVM's adaptability in modern AI contexts.

## Inference as a Continuous Process: Autonomous Agents and NVM

### Introduction: Rethinking Inference

The traditional idea of inference as a one-time event is changing. Instead, inference is an ongoing process in a feedback loop within autonomous agents.

### Autonomous Agents: Learning and Improving

Autonomous Agents continuously operate algorithms that learn, adapt, and proactively respond to user needs. These agents transcend static computation, offering dynamic engagement and iterative improvement.

### NVM's Role in Continuous Inference

NVM's attributes align with the needs of continuous inference. Unlike repetitive DNN inferences, which can be inefficient due to data transmission to the NPU, NVM's embedded computational capability supports ongoing, unobtrusive background knowledge discovery. Real-time tasks remain the domain of the NPU, while NVM emphasizes long-term efficiency.

As LLMs evolve, particularly with the maturation of RA-LLM algorithms, the prospect of leveraging NVM-based data stores on edge platforms emerges. This approach paves the way for a holistic, privacy-centric, efficient edge computing platform, functioning as an external memory and reasoning agent for human users.

## Conclusion

The deployment of Non-Volatile Memory (NVM) as a specialized accelerator within a System-on-Chip (SoC) marks a significant shift in the approach to modern computing. Moving away from the pursuit of absolute performance, the focus turns to long-term efficiency and strategic alignment with the demands of edge computing. NVM's specialized role enables continuous reasoning through a feedback loop and efficient execution at the edge. This configuration, concentrating on in-chip processing and minimizing unnecessary transmission of model weights, allows for the incorporation of user data updates while preserving privacy. By eliminating the need to run inferences in the cloud, NVM's deployment as an accelerator highlights a practical and thoughtful solution. It paves the way for technology to enhance our reasoning and memory securely and responsively.