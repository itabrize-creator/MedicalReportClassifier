import pandas as pd

# Sample medical report dataset
data = {
    "report": [
        # Cardiology
        "Patient presents with chest pain, shortness of breath, and palpitations. ECG shows abnormal rhythm. Diagnosed with arrhythmia.",
        "Echocardiogram reveals reduced ejection fraction. Patient has history of myocardial infarction. Prescribed beta blockers.",
        "Patient complaints of chest tightness and fatigue. Blood pressure is 160/100. Coronary artery disease suspected.",
        "Heart failure with preserved ejection fraction. Patient on diuretics and ACE inhibitors. Follow-up in 2 weeks.",
        "Troponin levels elevated. Patient admitted for suspected STEMI. Angioplasty performed successfully.",
        "Patient has atrial fibrillation with rapid ventricular response. Cardioversion considered.",
        "Hypertensive crisis observed. BP 200/120. IV labetalol administered.",
        "Mitral valve regurgitation noted on echo. Surgical consultation recommended.",

        # Neurology
        "MRI brain shows white matter lesions. Patient has history of multiple sclerosis. Prescribed interferon beta.",
        "Patient presents with sudden onset headache, nausea, vomiting. CT scan shows subarachnoid hemorrhage.",
        "Seizure episode lasting 3 minutes. EEG shows abnormal activity. Epilepsy diagnosed. Started on levetiracetam.",
        "Patient has tremors and rigidity. Bradykinesia observed. Parkinson's disease diagnosed.",
        "Stroke confirmed on MRI. Left sided weakness. Thrombolysis administered within 4 hours.",
        "Patient complains of severe migraine with aura. Prescribed sumatriptan.",
        "Dementia with memory loss and confusion. MMSE score 18/30. Alzheimer's suspected.",
        "Peripheral neuropathy with numbness in feet. Nerve conduction study abnormal.",

        # Orthopedics
        "X-ray shows fracture of the right femur. Surgery scheduled for internal fixation.",
        "Patient has lower back pain radiating to left leg. MRI shows L4-L5 disc herniation.",
        "Osteoarthritis of the knee with joint space narrowing. Physiotherapy recommended.",
        "Rotator cuff tear confirmed on MRI. Surgical repair advised.",
        "Patient presents with sports injury to ACL. Arthroscopic reconstruction planned.",
        "Bone density scan shows osteoporosis. Calcium and Vitamin D supplements prescribed.",
        "Scoliosis with 35 degree Cobb angle. Bracing initiated.",
        "Shoulder dislocation reduced successfully. Immobilization for 3 weeks.",

        # Radiology
        "CT chest shows 2cm pulmonary nodule in right lower lobe. Follow-up CT in 3 months recommended.",
        "Ultrasound abdomen reveals gallstones with thickened gallbladder wall. Cholecystitis suspected.",
        "MRI spine shows cord compression at C5-C6 level. Urgent neurosurgical referral.",
        "PET scan indicates hypermetabolic lesion in mediastinum. Lymphoma possible.",
        "X-ray pelvis shows hip fracture in elderly patient. Orthopedic referral made.",
        "Mammogram reveals suspicious microcalcifications in left breast. Biopsy recommended.",
        "Doppler ultrasound shows deep vein thrombosis in right leg. Anticoagulation started.",
        "CT abdomen shows appendix diameter 12mm with periappendiceal fat stranding. Appendicitis.",

        # Pathology
        "Biopsy of lymph node shows Reed-Sternberg cells. Hodgkin lymphoma confirmed.",
        "Blood smear shows hypersegmented neutrophils. Megaloblastic anemia diagnosed.",
        "Urine culture positive for E. coli. Sensitivity shows susceptibility to ciprofloxacin.",
        "Liver biopsy shows bridging fibrosis. Cirrhosis stage 3 confirmed.",
        "Fine needle aspiration of thyroid nodule shows follicular neoplasm. Surgery recommended.",
        "Bone marrow biopsy shows 30 percent blasts. Acute myeloid leukemia diagnosed.",
        "Sputum culture positive for Mycobacterium tuberculosis. Anti-TB therapy started.",
        "Histopathology of colon polyp shows adenocarcinoma. Staging CT ordered.",

        # General Medicine
        "Patient presents with fever, cough, and sore throat. Rapid strep test positive. Prescribed amoxicillin.",
        "Type 2 diabetes with HbA1c of 9.2. Metformin dose increased. Dietary counseling given.",
        "Hypothyroidism confirmed. TSH elevated at 12. Levothyroxine 50mcg prescribed.",
        "Patient with iron deficiency anemia. Hemoglobin 8.2. Oral iron supplements started.",
        "Urinary tract infection with dysuria and frequency. Urine dipstick positive. Nitrofurantoin prescribed.",
        "Asthma exacerbation. Peak flow 60 percent predicted. Nebulization and steroids given.",
        "Dengue fever confirmed with NS1 antigen positive. Supportive care, monitoring platelets.",
        "Hypertension with headache and dizziness. Amlodipine 5mg prescribed.",
    ],
    "category": (
        ["Cardiology"] * 8 +
        ["Neurology"] * 8 +
        ["Orthopedics"] * 8 +
        ["Radiology"] * 8 +
        ["Pathology"] * 8 +
        ["General Medicine"] * 8
    )
}

df = pd.DataFrame(data)
df.to_csv("medical_data.csv", index=False)
print("✅ Dataset created! medical_data.csv saved.")
print(df["category"].value_counts())