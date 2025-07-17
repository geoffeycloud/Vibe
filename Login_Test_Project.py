{
  "id": "1a45dbe7-b46a-49e7-bd82-309bcecb429b",
  "version": "2.0",
  "name": "Login Test Project",
  "url": "https://the-internet.herokuapp.com/login",
  "tests": [{
    "id": "23b34d3a-ae98-4c8b-8b59-ef33b21d7986",
    "name": "Valid Login",
    "commands": [{
      "id": "e716fdda-86dc-4dbc-b345-af4fb5f1f4fa",
      "comment": "",
      "command": "open",
      "target": "https://the-internet.herokuapp.com/login",
      "targets": [],
      "value": ""
    }, {
      "id": "b437cdd2-f286-4cd4-a079-138e1e4f0634",
      "comment": "",
      "command": "setWindowSize",
      "target": "697x720",
      "targets": [],
      "value": ""
    }, {
      "id": "5efef6ac-87d2-4520-9d0d-cbc499d2a8d3",
      "comment": "",
      "command": "click",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//form[@id='login']/div/div/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "713f78c1-1598-4857-bc46-ae82bc01cd49",
      "comment": "",
      "command": "click",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//form[@id='login']/div/div/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "921fca2e-56d3-4756-937a-02137bed1425",
      "comment": "",
      "command": "type",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//form[@id='login']/div/div/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "tomsmith"
    }, {
      "id": "1ffc49ef-0f66-4132-80ab-b5df97719e53",
      "comment": "",
      "command": "click",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//form[@id='login']/div[2]/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "6689b5a2-d401-4570-965b-78b055edb114",
      "comment": "",
      "command": "click",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//form[@id='login']/div[2]/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "cc9095e7-dc6a-40f9-b7fe-79fe4c91b288",
      "comment": "",
      "command": "type",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//form[@id='login']/div[2]/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/div/input", "xpath:position"]
      ],
      "value": "SuperSecretPassword!"
    }, {
      "id": "75993af2-d4f0-48d7-8d11-fd92eba43c66",
      "comment": "",
      "command": "click",
      "target": "css=.fa",
      "targets": [
        ["css=.fa", "css:finder"],
        ["xpath=//form[@id='login']/button/i", "xpath:idRelative"],
        ["xpath=//i", "xpath:position"],
        ["xpath=//i[contains(.,' Login')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "7a4bfa12-f2cd-41a7-914f-72cd96783a47",
      "comment": "",
      "command": "click",
      "target": "css=.icon-2x",
      "targets": [
        ["css=.icon-2x", "css:finder"],
        ["xpath=//div[@id='content']/div/a/i", "xpath:idRelative"],
        ["xpath=//a/i", "xpath:position"],
        ["xpath=//i[contains(.,'Logout')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "2e8140d5-132d-4706-a451-8176f317e87a",
      "comment": "",
      "command": "click",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//form[@id='login']/div/div/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "7d457c66-2996-4bf3-8861-6a054f79e71f",
      "comment": "",
      "command": "type",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//form[@id='login']/div/div/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "tomsmith"
    }, {
      "id": "33c7bb58-50ab-478c-aeb0-5dd956623be1",
      "comment": "",
      "command": "click",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//form[@id='login']/div[2]/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "eba56c9b-cf02-4d0e-8046-e4fa4c68cfc4",
      "comment": "",
      "command": "type",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//form[@id='login']/div[2]/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/div/input", "xpath:position"]
      ],
      "value": "pasword 27"
    }, {
      "id": "282e9514-218c-48d2-b782-0c718002e7f0",
      "comment": "",
      "command": "click",
      "target": "css=.fa",
      "targets": [
        ["css=.fa", "css:finder"],
        ["xpath=//form[@id='login']/button/i", "xpath:idRelative"],
        ["xpath=//i", "xpath:position"],
        ["xpath=//i[contains(.,' Login')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "f564d017-eeb7-4b40-a769-d442b89ace0f",
      "comment": "",
      "command": "click",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//form[@id='login']/div[2]/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/div/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "89e3395b-a791-40b6-a715-9dc21df12c6a",
      "comment": "",
      "command": "type",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//form[@id='login']/div[2]/div/input", "xpath:idRelative"],
        ["xpath=//div[2]/div/input", "xpath:position"]
      ],
      "value": "SuperSecretPassword!"
    }, {
      "id": "18279dbf-1eea-4cc8-aad5-05ea0aa4e50c",
      "comment": "",
      "command": "click",
      "target": "css=.fa",
      "targets": [
        ["css=.fa", "css:finder"],
        ["xpath=//form[@id='login']/button/i", "xpath:idRelative"],
        ["xpath=//i", "xpath:position"],
        ["xpath=//i[contains(.,' Login')]", "xpath:innerText"]
      ],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "4ecb9cd7-5b41-4334-af52-adecfa8c6a57",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["23b34d3a-ae98-4c8b-8b59-ef33b21d7986"]
  }],
  "urls": [],
  "plugins": []
}