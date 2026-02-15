from fpdf import FPDF

def main():
    pdf=FPDF(orientation="portrait",format="A4")
    pdf.add_page()
    pdf.set_page_background((210,296))
    pdf.set_font('helvetica',size=30)
    pdf.cell(text="CS50 Shirtificate",center=True)
    image_width=180
    x=(pdf.w-image_width)/2
    pdf.image("shirtificate.png",x=x,y=50,w=image_width)
    name=input("Name: ")
    pdf.set_font('helvetica',size=25)
    pdf.set_xy(10,110)
    pdf.set_text_color(255,255,255)
    pdf.cell(0,10,text=f"{name} took CS50",align="C")
    pdf.output("shirtificate.pdf")


if __name__=="__main__":
    main()
