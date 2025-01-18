import flet

def main(page: flet.Page):
    page.title = 'Bases'
    page.bgcolor: flet.Colors.BLUE_GREY_800 #Colors with capital letter
    #acepta rgb
    t1 = flet.Text('Otro texto',color='purple') #Text with capital letter
    page.add(flet.Text('App',size=25),t1) #se pueden varios en una sola carga

    def cambio_texto(x):
        t1.value = 'Otro otro texto'
        t1.color = 'red'
        page.update()
    
    btn = flet.FilledButton('Cambiar texto',on_click=cambio_texto) #la func sin ()
    page.add(btn)

if __name__ == '__main__':
        flet.app(main)
