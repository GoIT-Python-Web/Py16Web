def save_applicant_data(source, output):
    with open(output, "w", encoding="utf-8") as f:  #
        for applicant in source:  #
            f.write(  #
                #
                f"{applicant.get('name')},{applicant.get('specialty')},{applicant.get('math')},{applicant.get('lang')},{applicant.get('eng')}\n"
            )  #


applicant = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

if __name__ == '__main__':
    save_applicant_data(applicant, 'data.csv')
