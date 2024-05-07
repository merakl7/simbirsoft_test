import allure

def attach_csv_report(csv_file):
    allure.attach.file(csv_file, name="Transactions CSV", attachment_type=allure.attachment_type.CSV)
