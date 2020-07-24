import connectionSheet
import time
def readSheet(SpreadSheet,rangeNameSettings,service):
    valuesBooleans=None
    ban=True
    while ban:
        try:
            valuesBooleans = service.spreadsheets().values().get(spreadsheetId=SpreadSheet, range=rangeNameSettings,valueRenderOption='FORMATTED_VALUE').execute()
            ban=False
        except Exception as e:
            time.sleep(20)
            print(e)
    return valuesBooleans
def writeShhet(value,nameSheet,SpreadSheet,service):
    while True:
      TabName=nameSheet.split('!')[0]
      valuesR = []
      value_input_option = 'USER_ENTERED'
      valuesR.append(value)
      rangeNameSettings=nameSheet
      body = {
                  'values': value
      }
      request = service.spreadsheets().values().update(spreadsheetId=SpreadSheet, range=rangeNameSettings, valueInputOption=value_input_option, body=body)
      try:
          response = request.execute()
          break
      except Exception as e:
          print(e,'esperamos 20 s',TabName,SpreadSheet)
          time.sleep(20)
          writeShhet(value,nameSheet,SpreadSheet)
def copyTab(IdSheet,idSheetT,idSheetTCopy,service):
  # The ID of the sheet to copy.
  while True:

    sheet_id = idSheetT  # TODO: Update placeholder value.
    copy_sheet_to_another_spreadsheet_request_body = {
    'destination_spreadsheet_id': idSheetTCopy
    }
    request = service.spreadsheets().sheets().copyTo(spreadsheetId=IdSheet, sheetId=sheet_id, body=copy_sheet_to_another_spreadsheet_request_body)
    try:
        idsheetNew= request.execute()
        break
    except Exception as e:
        print(e,'esperamos 20 s')
        time.sleep(20)
        return copyTab(IdSheet,idSheetT,idSheetTCopy)

  idd=idsheetNew['sheetId']
  return idd
def deleteTab(sheetId,IdSheetData,service):
    while True:
      batch_update_spreadsheet_request_body = {
      "requests": [
      {
        "deleteSheet": {
          "sheetId": sheetId
        }
      }
    ]
      }
      request = service.spreadsheets().batchUpdate(spreadsheetId=IdSheetData, body=batch_update_spreadsheet_request_body)
      try:
          response = request.execute()
          break
      except Exception as e:
          print(e,'esperamos 20 s')
          time.sleep(20)
          pass
service=connectionSheet.get_service()
SpreadSheet='1jTsMmD_v6cRDw0JgRVL2nWwELRZZkFkDYfZTL83kyJA'
Tab='TestData'
rangeNameSettings=Tab+'!A1:D'
vals=readSheet(SpreadSheet,rangeNameSettings,service)
print(vals)
tip=copyTab(SpreadSheet,'0',SpreadSheet,service)
time.sleep(10)
deleteTab(tip,SpreadSheet,service)
rangeNameSettings=Tab+'!G1'

writeShhet([['Test Curso']],rangeNameSettings,SpreadSheet,service)
