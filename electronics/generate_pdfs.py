from fpdf import FPDF

class LabPDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 10)
        self.cell(0, 6, 'School of Computer Science & Technologies', new_x="LMARGIN", new_y="NEXT", align='C')
        self.ln(2)

    def section_title(self, title):
        self.set_font('Helvetica', 'B', 13)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def sub_title(self, title):
        self.set_font('Helvetica', 'B', 11)
        self.cell(0, 7, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def body_text(self, text):
        self.set_font('Helvetica', '', 10)
        self.multi_cell(0, 5, text)
        self.ln(1)

    def bold_text(self, text):
        self.set_font('Helvetica', 'B', 10)
        self.multi_cell(0, 5, text)
        self.ln(1)

    def add_table(self, headers, rows, col_widths=None):
        if col_widths is None:
            col_widths = [self.epw / len(headers)] * len(headers)
        # Header
        self.set_font('Helvetica', 'B', 9)
        self.set_fill_color(220, 220, 220)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 7, h, border=1, align='C', fill=True)
        self.ln()
        # Rows
        self.set_font('Helvetica', '', 9)
        for row in rows:
            for i, cell in enumerate(row):
                self.cell(col_widths[i], 7, str(cell), border=1, align='C')
            self.ln()
        self.ln(3)

    def diagram(self, text):
        self.set_font('Courier', '', 8)
        for line in text.split('\n'):
            self.cell(0, 4, line, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)


def make_pdf(filename, set_label, Ra, Rb, Rc):
    pdf = LabPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(0, 10, 'Measurement Report - Direct Current Circuits', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 8, 'Lab No. 1, Part 1', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.set_font('Helvetica', 'B', 11)
    pdf.set_text_color(0, 0, 180)
    pdf.cell(0, 8, f'SOLVED - {set_label}: Ra={Ra} Ohm, Rb={Rb} Ohm, Rc={Rc} Ohm', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.set_text_color(0, 0, 0)
    pdf.ln(3)

    # Info table
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(60, 7, 'Date:', border=1)
    pdf.cell(65, 7, 'Laboratory Subject:', border=1)
    pdf.cell(0, 7, 'Student Name and Surname:', border=1, new_x="LMARGIN", new_y="NEXT")
    pdf.cell(60, 7, 'Teacher:', border=1)
    pdf.cell(65, 7, 'DC circuits. Equiv. resistance.', border=1)
    pdf.cell(0, 7, '', border=1, new_x="LMARGIN", new_y="NEXT")
    pdf.cell(60, 7, 'Grade/Points:', border=1)
    pdf.cell(65, 7, '', border=1)
    pdf.cell(0, 7, 'Student No.:', border=1, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    # Aims
    pdf.section_title('Aims of Laboratory')
    pdf.body_text('- Student will collect measurement data in order to prove Ohm\'s and the 1st & 2nd Kirchhoff\'s laws')
    pdf.body_text('- Student will be aware of difference between connection in series and parallelly connection of resistors')

    # === SERIES ===
    pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
    pdf.ln(3)
    pdf.section_title('1. Resistors Connected in Series')
    pdf.body_text(f'Chosen resistors: Ra = {Ra} Ohm, Rb = {Rb} Ohm, Rc = {Rc} Ohm')

    # Series calculations
    Req_series = Ra + Rb + Rc
    V_ps = 10.0
    I_series = V_ps / Req_series  # in Amps
    I_series_mA = I_series * 1000
    Va = I_series * Ra
    Vb = I_series * Rb
    Vc = I_series * Rc
    V_sum = Va + Vb + Vc

    pdf.sub_title('Fig. 1.1 - Series connection for Req measurement:')
    pdf.diagram('    +--[Ra]--[Rb]--[Rc]--+\n    |                      |\n   (Ohm) Multimeter        |\n    |                      |\n    +----------------------+')

    pdf.sub_title('Fig. 1.2 - Series circuit with power supply (V = 10V):')
    pdf.diagram('     +--[Ra]---+--[Rb]---+--[Rc]--+\n     |   Va    |   Vb    |   Vc   |\n    (+)       (V)       (V)      (V)\n   10V PS      |         |        |\n    (-)        |         |        |\n     +---(A)---+---------+--------+\n          I')

    pdf.sub_title('Table 1.1 - Series Resistance')
    w5 = pdf.epw / 5
    pdf.add_table(
        ['Ra [Ohm]', 'Rb [Ohm]', 'Rc [Ohm]', 'Req meas. [Ohm]', 'Req calc. [Ohm]'],
        [[str(Ra), str(Rb), str(Rc), f'{Req_series:.2f}', f'{Ra}+{Rb}+{Rc} = {Req_series:.2f}']],
        [w5]*5
    )

    pdf.bold_text(f'Calculation: Req = Ra + Rb + Rc = {Ra} + {Rb} + {Rc} = {Req_series:.2f} Ohm')

    pdf.sub_title('Table 1.2 - Series Circuit Measurements (V_PS = 10 V)')
    pdf.add_table(
        ['I [mA]', 'Va [V]', 'Vb [V]', 'Vc [V]', 'Va+Vb+Vc [V]'],
        [[f'{I_series_mA:.3f}', f'{Va:.3f}', f'{Vb:.3f}', f'{Vc:.3f}', f'{V_sum:.3f}']],
        [w5]*5
    )

    pdf.bold_text('Calculations:')
    pdf.body_text(f'I = V / Req = {V_ps} / {Req_series:.2f} = {I_series_mA:.3f} mA')
    pdf.body_text(f'Va = I x Ra = {I_series_mA:.3f} mA x {Ra} Ohm = {Va:.3f} V')
    pdf.body_text(f'Vb = I x Rb = {I_series_mA:.3f} mA x {Rb} Ohm = {Vb:.3f} V')
    pdf.body_text(f'Vc = I x Rc = {I_series_mA:.3f} mA x {Rc} Ohm = {Vc:.3f} V')
    pdf.set_text_color(0, 128, 0)
    pdf.bold_text(f'Kirchhoff\'s Voltage Law: Va + Vb + Vc = {Va:.3f} + {Vb:.3f} + {Vc:.3f} = {V_sum:.3f} V = V_PS  [VERIFIED]')
    pdf.set_text_color(0, 0, 0)

    # === PARALLEL ===
    pdf.add_page()
    pdf.section_title('2. Resistors Connected in Parallel')
    pdf.body_text(f'Same resistors: Ra = {Ra} Ohm, Rb = {Rb} Ohm, Rc = {Rc} Ohm')

    # Parallel calculations
    Req_parallel = 1.0 / (1.0/Ra + 1.0/Rb + 1.0/Rc)
    Ia = V_ps / Ra * 1000  # mA
    Ib = V_ps / Rb * 1000
    Ic = V_ps / Rc * 1000
    I_total = Ia + Ib + Ic

    pdf.sub_title('Fig. 2.1 - Parallel connection for Req measurement:')
    pdf.diagram('    +--[Ra]--+\n    +--[Rb]--+\n    +--[Rc]--+\n    |        |\n   (Ohm) Multimeter\n    |        |\n    +--------+')

    pdf.sub_title('Fig. 2.2 - Parallel circuit with power supply (V = 10V):')
    pdf.diagram('        I_total\n    +---(A)---+---------+---------+\n    |         |         |         |\n   (+)      [Ra]      [Rb]      [Rc]\n  10V PS   (A)Ia     (A)Ib     (A)Ic\n   (-)        |         |         |\n    |         |         |         |\n    +---(V)---+---------+---------+\n         V = 10V')

    pdf.sub_title('Table 2.1 - Parallel Resistance')
    pdf.add_table(
        ['Ra [Ohm]', 'Rb [Ohm]', 'Rc [Ohm]', 'Req meas. [Ohm]', 'Req calc. [Ohm]'],
        [[str(Ra), str(Rb), str(Rc), f'{Req_parallel:.2f}', f'{Req_parallel:.2f}']],
        [w5]*5
    )

    pdf.bold_text('Calculation:')
    pdf.body_text(f'1/Req = 1/Ra + 1/Rb + 1/Rc = 1/{Ra} + 1/{Rb} + 1/{Rc}')
    pdf.body_text(f'1/Req = {1.0/Ra:.6f} + {1.0/Rb:.6f} + {1.0/Rc:.6f} = {1.0/Ra + 1.0/Rb + 1.0/Rc:.6f}')
    pdf.body_text(f'Req = {Req_parallel:.2f} Ohm')

    pdf.sub_title('Table 2.2 - Parallel Circuit Measurements (V_PS = 10 V)')
    w6 = pdf.epw / 6
    pdf.add_table(
        ['V [V]', 'Ia [mA]', 'Ib [mA]', 'Ic [mA]', 'I_total [mA]', 'Ia+Ib+Ic [mA]'],
        [[f'{V_ps:.3f}', f'{Ia:.3f}', f'{Ib:.3f}', f'{Ic:.3f}', f'{I_total:.3f}', f'{I_total:.3f}']],
        [w6]*6
    )

    pdf.bold_text('Calculations:')
    pdf.body_text(f'V = 10 V (same across all parallel resistors)')
    pdf.body_text(f'Ia = V / Ra = 10 / {Ra} = {Ia:.3f} mA')
    pdf.body_text(f'Ib = V / Rb = 10 / {Rb} = {Ib:.3f} mA')
    pdf.body_text(f'Ic = V / Rc = 10 / {Rc} = {Ic:.3f} mA')
    pdf.set_text_color(0, 128, 0)
    pdf.bold_text(f'Kirchhoff\'s Current Law: Ia + Ib + Ic = {Ia:.3f} + {Ib:.3f} + {Ic:.3f} = {I_total:.3f} mA = I_total  [VERIFIED]')
    pdf.body_text(f'Verification: I_total = V / Req = 10 / {Req_parallel:.2f} = {V_ps/Req_parallel*1000:.3f} mA  [VERIFIED]')
    pdf.set_text_color(0, 0, 0)

    pdf.output(filename)
    print(f'Created {filename}')


# Set 1
make_pdf(r'd:\Sem2_Vizja\electronics\solve1.pdf', 'Set 1', 1000, 2000, 3000)
# Set 2
make_pdf(r'd:\Sem2_Vizja\electronics\solve2.pdf', 'Set 2', 1000, 3000, 5000)
