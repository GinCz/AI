# EU AI Act (Regulation (EU) 2024/1689) Risk Classification Matrix

A developer and executive operational guide to classifying artificial intelligence systems under the European Artificial Intelligence Act.

---

## 1. Risk Tier Hierarchy

```
       ▲  [Unacceptable Risk] -> STRICTLY PROHIBITED (Article 5)
      / \
     /   \  [High Risk] -> Strict Conformity Assessment & CE Marking (Articles 6-49)
    /     \
   /       \  [Specific Transparency Risk] -> Mandatory Disclosure & Watermarking (Article 50)
  /         \
 /           \  [Minimal / No Risk] -> Unregulated / Voluntary Codes of Conduct (Article 95)
 --------------
```

---

## 2. Classification & Requirements Checklist

| Risk Category | Examples | Statutory Obligations |
| :--- | :--- | :--- |
| **Prohibited AI** | - Subliminal cognitive behavioral manipulation.<br>- Social scoring by public/private bodies.<br>- Emotion recognition in workplace/education.<br>- Untargeted scraping of facial images from web/CCTV.<br>- Biometric categorization for sensitive traits. | **Banned from placement on EU market.** Statutory fines up to **€35M or 7% of global turnover**. |
| **High-Risk AI (Annex III)** | - Critical infrastructure management.<br>- Employment, recruitment, and worker evaluation.<br>- Credit scoring and risk evaluation of natural persons.<br>- Life/health insurance underwriting.<br>- Law enforcement and judicial administration.<br>- Essential public services eligibility. | - Continuous Risk Management System (Article 9).<br>- High-quality governance of training datasets (Article 10).<br>- Detailed technical documentation & logging (Articles 11-12).<br>- Human oversight mechanisms (Article 14).<br>- High cybersecurity and accuracy standards (Article 15).<br>- Conformity assessment & CE marking.<br>- Registration in EU High-Risk Database. |
| **General Purpose AI (GPAI)** | - LLMs and foundation models (e.g. Gemini, GPT, Claude, Llama).<br>- Models with compute > $10^{25}$ FLOPs classify as **Systemic Risk GPAI**. | - Technical documentation for downstream providers.<br>- Summary of training data copyright compliance.<br>- Systemic models: Model evaluation, red-teaming, energy efficiency reporting, incident notification to AI Office. |
| **Transparency Risk** | - AI chatbots and conversational agents.<br>- Deepfakes and AI-generated image/audio/video.<br>- AI-generated text published for public information. | - Inform users that they are interacting with AI.<br>- Machine-readable watermarking / metadata tagging of synthetic media.<br>- Clear labeling of deepfakes. |
| **Minimal / No Risk** | - AI-enabled video games.<br>- Spam filters and search rankings.<br>- Inventory optimization algorithms.<br>- Standard code completion (syntax). | No mandatory restrictions; free deployment across the EU Single Market. |
