from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from POKE_API import get_pokemon_info

root = Tk()
root.title("Displaying Pokemon Info")
root.resizable(False, False)
# TODO: Additional window configuration

# Add frame to window
frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

frm_btm_left = ttk.LabelFrame(root, text='info')
frm_btm_left.grid(row=1, column=0, sticky=N, padx=(10, 0))

frm_btm_right = ttk.LabelFrame(root, text='Stats')
frm_btm_right.grid(row=1, column=1, sticky=N, padx=10, pady=(0, 10))

# Add widgets to top frame
lbl_name = ttk.Label(frm_top, text='Pokemon Name:')
lbl_name.grid(row=0, column=0)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1, padx=10)

def handle_get_info_btn_click():
    #Get the name of the Pokemon
    poke_name = ent_name.get().strip()
    if poke_name == '':
        return
    # Get the Pokemon info from the PokeAPI
    poke_info =  get_pokemon_info(poke_name)
    if poke_info is None:
        error_message = f"Unable to get the information from the POKE_API for {poke_name}"
        messagebox.showinfo(title='Error', message=error_message, icon='error')
        return

    #Populate the info values
    lbl_height_value['text'] = f"{poke_info['height']} dm"

    prg_hp['value'] = poke_info['stats'][0]['base_stat']
    prg_attack['value'] = poke_info['stats'][1]['base_stat']
    prg_defense['value'] =  poke_info['stats'][2]['base_stat']
    prg_SA['value'] = poke_info['stats'][3]['base_stat']
    prg_SD['value'] = poke_info['stats'][4]['base_stat']
    prg_Speed['value'] = poke_info['stats'][5]['base_stat']
    return

btn_get_info = ttk.Button(frm_top, text='Get Info', command=handle_get_info_btn_click)
btn_get_info.grid(row=0, column=2)

#Add widget to bottom left frame
lbl_height = ttk.Label(frm_btm_left, text='Height:')
lbl_height.grid(row=0, column=0, sticky=E)

lbl_height_value = ttk.Label(frm_btm_left, text='TBD')
lbl_height_value.grid(row=0, column=1)

#Add widget to bottom right frame
lbl_hp = ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=1, column=0, sticky=E)
prg_hp = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_hp.grid(row=1, column=1)

lbl_attack = ttk.Label(frm_btm_right, text='Attack: ')
lbl_attack.grid(row=2, column=0, sticky=E, pady=(0,5))
prg_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_attack.grid(row=2, column=1, pady=5, padx=(0,5))


lbl_defense = ttk.Label(frm_btm_right, text='Defense: ')
lbl_defense.grid(row=3, column=0, sticky=E, pady=(0,5))
prg_defense = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_defense.grid(row=3, column=1, pady=(0,5), padx=(0,5))

lbl_SA = ttk.Label(frm_btm_right, text='Special Attack:')
lbl_SA.grid(row=4, column=0, sticky=E, pady=(0,5))
prg_SA = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_SA.grid(row=4, column=1, pady=(0,5), padx=(0,5))

lbl_SD = ttk.Label(frm_btm_right, text='Special Defense:')
lbl_SD.grid(row=5, column=0, sticky=E, pady=(0,5))
prg_SD = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_SD.grid(row=5, column=1, pady=(0,5), padx=(0,5))

lbl_Speed = ttk.Label(frm_btm_right, text='Speed:')
lbl_Speed.grid(row=6, column=0, sticky=E, pady=(0,5))
prg_Speed = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_Speed.grid(row=6, column=1, pady=(0,5), padx=(0,5))

# Loop until window is closed

root.mainloop()