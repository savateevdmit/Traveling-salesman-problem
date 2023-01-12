checkboxs = """
MDFloatLayout:
    MDCheckbox:
        group: 'group'
        pos_hint: {"center_x": .6, "center_y": 0.8}
        size_hint: .1, .1
        on_active: app.check(*args)
        
    MDCheckbox:
        group: 'group'
        pos_hint: {"center_x": .6, "center_y": 0.7}
        size_hint: .1, .1
        on_active: app.check1(*args)
"""