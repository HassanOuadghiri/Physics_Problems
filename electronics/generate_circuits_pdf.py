import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import schemdraw
import schemdraw.elements as elm

# =====================================================================
# HELPER: Draw series circuit schematic
# =====================================================================
def draw_series_circuit(Ra, Rb, Rc, title):
    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=13)
        d += elm.SourceV().up().label('10V', loc='left')
        d += elm.Line().right()
        d += elm.Ammeter().right().label('A', loc='top')
        d += elm.Line().right()

        ra = d.add(elm.Resistor().right().label(f'Ra\n{Ra}Ω', loc='top'))
        d += elm.Line().right(d.unit * 0.3)
        rb = d.add(elm.Resistor().right().label(f'Rb\n{Rb}Ω', loc='top'))
        d += elm.Line().right(d.unit * 0.3)
        rc = d.add(elm.Resistor().right().label(f'Rc\n{Rc}Ω', loc='top'))

        d += elm.Line().down()
        d += elm.Line().left().tox(d.elements[0].start)
        d += elm.Line().up().toy(d.elements[0].start)

        # Add voltmeter labels
        d += elm.CurrentLabelInline(direction='in').at(d.elements[2]).label('I')

    fig = d.get_imagedata('svg')
    # Use schemdraw's matplotlib figure
    d2 = schemdraw.Drawing(show=False)
    d2.config(fontsize=13)
    d2 += elm.SourceV().up().label('10V', loc='left')
    d2 += elm.Line().right()
    d2 += elm.Ammeter().right().label('A', loc='top')
    d2 += elm.Line().right(d2.unit * 0.2)
    d2 += elm.Resistor().right().label(f'Ra={Ra}Ω', loc='top')
    d2 += elm.Line().right(d2.unit * 0.2)
    d2 += elm.Resistor().right().label(f'Rb={Rb}Ω', loc='top')
    d2 += elm.Line().right(d2.unit * 0.2)
    d2 += elm.Resistor().right().label(f'Rc={Rc}Ω', loc='top')
    d2 += elm.Line().down()
    d2 += elm.Line().left().tox(0)
    d2 += elm.Line().up().toy(0)
    fig_ax = d2.draw()
    fig_obj = fig_ax.get_figure()
    fig_obj.suptitle(title, fontsize=14, fontweight='bold', y=0.98)
    return fig_obj


def draw_series_circuit_simple(Ra, Rb, Rc, title):
    """Draw series circuit using matplotlib directly"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 4))
    ax.set_xlim(-1, 13)
    ax.set_ylim(-2, 4)
    ax.set_aspect('equal')
    ax.axis('off')
    fig.suptitle(title, fontsize=14, fontweight='bold')

    # Power supply
    ax.plot([0, 0], [0, 3], 'k-', linewidth=2)
    ax.annotate('+ 10V -', xy=(-0.5, 1.5), fontsize=11, fontweight='bold', ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', edgecolor='black'))

    # Top wire
    ax.plot([0, 1.5], [3, 3], 'k-', linewidth=2)

    # Ammeter
    circle_a = plt.Circle((2, 3), 0.4, fill=False, edgecolor='blue', linewidth=2)
    ax.add_patch(circle_a)
    ax.text(2, 3, 'A', ha='center', va='center', fontsize=11, color='blue', fontweight='bold')
    ax.plot([2.4, 3], [3, 3], 'k-', linewidth=2)

    # Draw resistor boxes
    resistors = [(Ra, 'Ra'), (Rb, 'Rb'), (Rc, 'Rc')]
    colors = ['#FFB3B3', '#B3D9FF', '#B3FFB3']
    x_pos = 3
    for i, (R, name) in enumerate(resistors):
        rect = patches.FancyBboxPatch((x_pos, 2.5), 2, 1, boxstyle="round,pad=0.1",
                                       facecolor=colors[i], edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x_pos + 1, 3, f'{name}\n{R}Ω', ha='center', va='center', fontsize=10, fontweight='bold')

        # Voltmeter below
        vm_y = 1.0
        ax.plot([x_pos + 0.2, x_pos + 0.2], [2.5, vm_y + 0.4], 'b--', linewidth=1)
        ax.plot([x_pos + 1.8, x_pos + 1.8], [2.5, vm_y + 0.4], 'b--', linewidth=1)
        circle_v = plt.Circle((x_pos + 1, vm_y), 0.35, fill=False, edgecolor='red', linewidth=1.5)
        ax.add_patch(circle_v)
        ax.text(x_pos + 1, vm_y, 'V', ha='center', va='center', fontsize=9, color='red', fontweight='bold')
        ax.plot([x_pos + 0.2, x_pos + 0.65], [vm_y, vm_y], 'b--', linewidth=1)
        ax.plot([x_pos + 1.35, x_pos + 1.8], [vm_y, vm_y], 'b--', linewidth=1)

        if i < 2:
            ax.plot([x_pos + 2, x_pos + 2.5], [3, 3], 'k-', linewidth=2)
        x_pos += 2.5

    # Close circuit
    ax.plot([x_pos - 0.5 + 2, x_pos - 0.5 + 2], [3, 0], 'k-', linewidth=2)
    ax.plot([0, x_pos - 0.5 + 2], [0, 0], 'k-', linewidth=2)

    # Current arrow
    ax.annotate('', xy=(1.5, 3.6), xytext=(0.3, 3.6),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax.text(0.9, 3.85, 'I', fontsize=12, color='green', fontweight='bold', ha='center')

    plt.tight_layout()
    return fig


def draw_parallel_circuit_simple(Ra, Rb, Rc, title):
    """Draw parallel circuit using matplotlib directly"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    ax.set_xlim(-1, 13)
    ax.set_ylim(-1, 7)
    ax.set_aspect('equal')
    ax.axis('off')
    fig.suptitle(title, fontsize=14, fontweight='bold')

    # Power supply on the left
    ax.plot([0, 0], [0, 6], 'k-', linewidth=2)
    ax.annotate('+ 10V -', xy=(-0.5, 3), fontsize=11, fontweight='bold', ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', edgecolor='black'))

    # Top wire with ammeter
    ax.plot([0, 1.5], [6, 6], 'k-', linewidth=2)
    circle_a = plt.Circle((2, 6), 0.4, fill=False, edgecolor='blue', linewidth=2)
    ax.add_patch(circle_a)
    ax.text(2, 6, 'A', ha='center', va='center', fontsize=11, color='blue', fontweight='bold')
    ax.text(2, 6.6, 'I_total', ha='center', va='center', fontsize=9, color='blue')
    ax.plot([2.4, 3], [6, 6], 'k-', linewidth=2)

    # Junction point top
    ax.plot(3, 6, 'ko', markersize=6)

    # Three parallel branches
    resistors = [(Ra, 'Ra'), (Rb, 'Rb'), (Rc, 'Rc')]
    colors = ['#FFB3B3', '#B3D9FF', '#B3FFB3']
    branch_x = [4, 7, 10]

    for i, (R, name) in enumerate(resistors):
        bx = branch_x[i]
        # Top connection
        ax.plot([3, bx], [6, 6], 'k-', linewidth=2)
        ax.plot([bx, bx], [6, 4.5], 'k-', linewidth=2)

        # Resistor
        rect = patches.FancyBboxPatch((bx - 0.8, 3.2), 1.6, 1.3, boxstyle="round,pad=0.1",
                                       facecolor=colors[i], edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(bx, 3.85, f'{name}\n{R}Ω', ha='center', va='center', fontsize=10, fontweight='bold')

        # Ammeter in branch
        ax.plot([bx, bx], [3.2, 2.2], 'k-', linewidth=2)
        circle_ai = plt.Circle((bx, 1.8), 0.35, fill=False, edgecolor='blue', linewidth=1.5)
        ax.add_patch(circle_ai)
        ax.text(bx, 1.8, 'A', ha='center', va='center', fontsize=9, color='blue', fontweight='bold')
        ax.text(bx + 0.6, 1.8, f'I_{name[1].lower()}', ha='left', va='center', fontsize=9, color='blue')

        # Bottom connection
        ax.plot([bx, bx], [1.45, 0], 'k-', linewidth=2)
        ax.plot([3, bx], [0, 0], 'k-', linewidth=2)

    # Junction point bottom
    ax.plot(3, 0, 'ko', markersize=6)

    # Voltmeter across all
    ax.plot([3, 3], [6, 0], 'k-', linewidth=2)
    ax.plot([0, 3], [0, 0], 'k-', linewidth=2)

    # Voltmeter symbol between junctions
    circle_v = plt.Circle((1.5, 0), 0.35, fill=False, edgecolor='red', linewidth=1.5)
    ax.add_patch(circle_v)
    ax.text(1.5, 0, 'V', ha='center', va='center', fontsize=9, color='red', fontweight='bold')
    ax.text(1.5, -0.6, '10V', ha='center', fontsize=9, color='red')

    # Current arrow
    ax.annotate('', xy=(1.5, 6.5), xytext=(0.3, 6.5),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax.text(0.9, 6.8, 'I', fontsize=12, color='green', fontweight='bold', ha='center')

    plt.tight_layout()
    return fig


def draw_series_req_circuit(Ra, Rb, Rc, title):
    """Draw series connection for Req measurement (Fig 1.1)"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 3.5))
    ax.set_xlim(-1, 13)
    ax.set_ylim(-1, 4)
    ax.set_aspect('equal')
    ax.axis('off')
    fig.suptitle(title, fontsize=14, fontweight='bold')

    # Top wire
    ax.plot([0, 0], [0, 3], 'k-', linewidth=2)
    ax.plot([0, 2], [3, 3], 'k-', linewidth=2)

    # Resistors in series
    resistors = [(Ra, 'Ra'), (Rb, 'Rb'), (Rc, 'Rc')]
    colors = ['#FFB3B3', '#B3D9FF', '#B3FFB3']
    x_pos = 2
    for i, (R, name) in enumerate(resistors):
        rect = patches.FancyBboxPatch((x_pos, 2.5), 2, 1, boxstyle="round,pad=0.1",
                                       facecolor=colors[i], edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(x_pos + 1, 3, f'{name}\n{R}Ω', ha='center', va='center', fontsize=10, fontweight='bold')
        if i < 2:
            ax.plot([x_pos + 2, x_pos + 2.5], [3, 3], 'k-', linewidth=2)
        x_pos += 2.5

    end_x = x_pos - 0.5 + 2
    ax.plot([x_pos - 0.5, end_x], [3, 3], 'k-', linewidth=2)
    ax.plot([end_x, end_x], [3, 0], 'k-', linewidth=2)
    ax.plot([0, end_x], [0, 0], 'k-', linewidth=2)

    # Ohmmeter
    circle_ohm = plt.Circle((0, 1.5), 0.5, fill=False, edgecolor='purple', linewidth=2)
    ax.add_patch(circle_ohm)
    ax.text(0, 1.5, 'Ω', ha='center', va='center', fontsize=14, color='purple', fontweight='bold')
    ax.text(-0.8, 1.5, 'Multimeter', ha='right', va='center', fontsize=9, color='purple')

    Req = Ra + Rb + Rc
    ax.text(5, -0.6, f'Req = {Ra} + {Rb} + {Rc} = {Req} Ω', ha='center', fontsize=12,
            fontweight='bold', color='darkblue')

    plt.tight_layout()
    return fig


def draw_parallel_req_circuit(Ra, Rb, Rc, title):
    """Draw parallel connection for Req measurement (Fig 2.1)"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.set_xlim(-2, 8)
    ax.set_ylim(-1.5, 7)
    ax.set_aspect('equal')
    ax.axis('off')
    fig.suptitle(title, fontsize=14, fontweight='bold')

    # Left wire
    ax.plot([0, 0], [0, 6], 'k-', linewidth=2)
    # Right wire
    ax.plot([6, 6], [0, 6], 'k-', linewidth=2)

    # Three parallel resistors
    resistors = [(Ra, 'Ra'), (Rb, 'Rb'), (Rc, 'Rc')]
    colors = ['#FFB3B3', '#B3D9FF', '#B3FFB3']
    y_positions = [5, 3, 1]

    for i, (R, name) in enumerate(resistors):
        y = y_positions[i]
        ax.plot([0, 1.5], [y, y], 'k-', linewidth=2)
        rect = patches.FancyBboxPatch((1.5, y - 0.4), 3, 0.8, boxstyle="round,pad=0.1",
                                       facecolor=colors[i], edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        ax.text(3, y, f'{name} = {R}Ω', ha='center', va='center', fontsize=10, fontweight='bold')
        ax.plot([4.5, 6], [y, y], 'k-', linewidth=2)

    # Ohmmeter at bottom
    ax.plot([0, 2.5], [0, 0], 'k-', linewidth=2)
    ax.plot([3.5, 6], [0, 0], 'k-', linewidth=2)
    circle_ohm = plt.Circle((3, 0), 0.45, fill=False, edgecolor='purple', linewidth=2)
    ax.add_patch(circle_ohm)
    ax.text(3, 0, 'Ω', ha='center', va='center', fontsize=14, color='purple', fontweight='bold')

    Req = 1.0 / (1.0/Ra + 1.0/Rb + 1.0/Rc)
    ax.text(3, -1, f'Req = 1/(1/{Ra} + 1/{Rb} + 1/{Rc}) = {Req:.2f} Ω', ha='center',
            fontsize=11, fontweight='bold', color='darkblue')

    plt.tight_layout()
    return fig


def draw_voltage_distribution_series(Ra, Rb, Rc, V_ps=10.0):
    """Draw voltage potential graph for series circuit"""
    Req = Ra + Rb + Rc
    I = V_ps / Req
    Va = I * Ra
    Vb = I * Rb
    Vc = I * Rc

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle(f'Series Circuit Analysis (Ra={Ra}Ω, Rb={Rb}Ω, Rc={Rc}Ω)', fontsize=14, fontweight='bold')

    # Voltage potential graph (staircase)
    positions = [0, 1, 2, 3, 4]
    labels = ['Start\n(0V)', f'After\nSource\n(+{V_ps}V)', f'After Ra\n(-{Va:.2f}V)',
              f'After Rb\n(-{Vb:.2f}V)', f'After Rc\n(-{Vc:.2f}V)']
    potentials = [0, V_ps, V_ps - Va, V_ps - Va - Vb, V_ps - Va - Vb - Vc]

    colors_bar = ['gray', '#2ecc71', '#e74c3c', '#3498db', '#9b59b6']
    ax1.bar(positions, potentials, color=colors_bar, edgecolor='black', width=0.6, alpha=0.8)

    # Connect with lines
    for i in range(len(positions) - 1):
        ax1.plot([positions[i] + 0.3, positions[i+1] - 0.3], [potentials[i], potentials[i+1]],
                'k--', linewidth=1.5, alpha=0.5)

    # Voltage drop annotations
    drops = [('Source\n+10V', 0, 1, V_ps), (f'Ra\n-{Va:.2f}V', 1, 2, -Va),
             (f'Rb\n-{Vb:.2f}V', 2, 3, -Vb), (f'Rc\n-{Vc:.2f}V', 3, 4, -Vc)]
    for label, i1, i2, dv in drops:
        mid_x = (positions[i1] + positions[i2]) / 2
        mid_y = (potentials[i1] + potentials[i2]) / 2
        color = '#2ecc71' if dv > 0 else '#e74c3c'
        ax1.annotate(label, xy=(mid_x, mid_y + 0.3), fontsize=8, ha='center',
                    color=color, fontweight='bold')

    ax1.set_xlabel('Circuit Position', fontsize=11)
    ax1.set_ylabel('Potential (V)', fontsize=11)
    ax1.set_title('Voltage Potential Along Series Circuit', fontsize=12, fontweight='bold')
    ax1.set_xticks(positions)
    ax1.set_xticklabels(['GND', 'Source', 'Ra', 'Rb', 'Rc'], fontsize=9)
    ax1.axhline(y=0, color='gray', linestyle='-', linewidth=0.5)
    ax1.grid(axis='y', alpha=0.3)

    # Voltage drops bar chart
    components = ['Va (Ra)', 'Vb (Rb)', 'Vc (Rc)']
    voltage_drops = [Va, Vb, Vc]
    bars = ax2.bar(components, voltage_drops, color=['#FFB3B3', '#B3D9FF', '#B3FFB3'],
                   edgecolor='black', linewidth=1.5)

    for bar, v in zip(bars, voltage_drops):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'{v:.3f} V', ha='center', fontsize=11, fontweight='bold')

    ax2.axhline(y=V_ps, color='red', linestyle='--', linewidth=1.5, label=f'V_PS = {V_ps}V')
    ax2.set_ylabel('Voltage (V)', fontsize=11)
    ax2.set_title('Voltage Drops Across Resistors', fontsize=12, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.set_ylim(0, V_ps * 1.2)
    ax2.grid(axis='y', alpha=0.3)

    # Add sum annotation
    ax2.text(1, V_ps + 0.3, f'Sum = {sum(voltage_drops):.3f} V (= V_PS ✓)',
            ha='center', fontsize=10, color='green', fontweight='bold')

    plt.tight_layout()
    return fig


def draw_current_distribution_parallel(Ra, Rb, Rc, V_ps=10.0):
    """Draw current distribution graph for parallel circuit"""
    Ia = V_ps / Ra * 1000  # mA
    Ib = V_ps / Rb * 1000
    Ic = V_ps / Rc * 1000
    I_total = Ia + Ib + Ic
    Req = 1.0 / (1.0/Ra + 1.0/Rb + 1.0/Rc)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle(f'Parallel Circuit Analysis (Ra={Ra}Ω, Rb={Rb}Ω, Rc={Rc}Ω)', fontsize=14, fontweight='bold')

    # Current distribution bar chart
    components = ['Ia (Ra)', 'Ib (Rb)', 'Ic (Rc)', 'I_total']
    currents = [Ia, Ib, Ic, I_total]
    colors_c = ['#FFB3B3', '#B3D9FF', '#B3FFB3', '#FFD700']
    bars = ax1.bar(components, currents, color=colors_c, edgecolor='black', linewidth=1.5)

    for bar, c in zip(bars, currents):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
                f'{c:.3f} mA', ha='center', fontsize=10, fontweight='bold')

    ax1.set_ylabel('Current (mA)', fontsize=11)
    ax1.set_title('Current Distribution in Parallel Branches', fontsize=12, fontweight='bold')
    ax1.grid(axis='y', alpha=0.3)

    # Add KCL verification
    ax1.text(1.5, max(currents) * 0.5, f'KCL: Ia + Ib + Ic = I_total\n'
             f'{Ia:.3f} + {Ib:.3f} + {Ic:.3f} = {I_total:.3f} mA ✓',
             ha='center', fontsize=10, color='green', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', edgecolor='green'))

    # Pie chart of current distribution
    branch_currents = [Ia, Ib, Ic]
    labels_pie = [f'Ia = {Ia:.2f} mA\n({Ia/I_total*100:.1f}%)',
                  f'Ib = {Ib:.2f} mA\n({Ib/I_total*100:.1f}%)',
                  f'Ic = {Ic:.2f} mA\n({Ic/I_total*100:.1f}%)']
    colors_pie = ['#FFB3B3', '#B3D9FF', '#B3FFB3']
    explode = (0.05, 0.05, 0.05)

    wedges, texts, autotexts = ax2.pie(branch_currents, labels=labels_pie, colors=colors_pie,
                                        explode=explode, autopct='', startangle=90,
                                        wedgeprops=dict(edgecolor='black', linewidth=1.5))
    for t in texts:
        t.set_fontsize(9)
        t.set_fontweight('bold')

    ax2.set_title(f'Current Split (I_total = {I_total:.2f} mA)', fontsize=12, fontweight='bold')

    plt.tight_layout()
    return fig


def draw_potential_map_series(Ra, Rb, Rc, V_ps=10.0):
    """Draw the potential along the series circuit as a continuous line graph"""
    Req = Ra + Rb + Rc
    I = V_ps / Req
    Va = I * Ra
    Vb = I * Rb
    Vc = I * Rc

    fig, ax = plt.subplots(figsize=(10, 5))

    # Define circuit positions (normalized)
    x = [0, 0.5, 1.5, 1.5+1, 1.5+1+1, 1.5+1+1+1, 1.5+1+1+1+0.5]
    v = [0, 0, V_ps, V_ps - Va, V_ps - Va - Vb, V_ps - Va - Vb - Vc, 0]
    labels_x = ['GND', 'Wire', 'Source\n(+10V)', f'Node A→B\n{V_ps-Va:.2f}V',
                f'Node B→C\n{V_ps-Va-Vb:.2f}V', f'Node C→GND\n{0:.2f}V', 'GND']

    ax.plot(x, v, 'b-o', linewidth=2.5, markersize=8, color='#2c3e50')

    # Fill regions
    ax.fill_between(x[1:3], [0, 0], v[1:3], alpha=0.2, color='green', label='Source (+10V)')
    ax.fill_between(x[2:4], [0, 0], v[2:4], alpha=0.2, color='red', label=f'Ra drop ({Va:.2f}V)')
    ax.fill_between(x[3:5], [0, 0], v[3:5], alpha=0.2, color='blue', label=f'Rb drop ({Vb:.2f}V)')
    ax.fill_between(x[4:6], [0, 0], v[4:6], alpha=0.2, color='purple', label=f'Rc drop ({Vc:.2f}V)')

    # Annotate voltage drops
    arrows = [(2, 3, Va, 'Ra'), (3, 4, Vb, 'Rb'), (4, 5, Vc, 'Rc')]
    for i1, i2, dv, name in arrows:
        mid_x = (x[i1] + x[i2]) / 2
        ax.annotate('', xy=(mid_x, v[i2]), xytext=(mid_x, v[i1]),
                    arrowprops=dict(arrowstyle='<->', color='red', lw=2))
        ax.text(mid_x + 0.15, (v[i1] + v[i2]) / 2, f'ΔV={dv:.2f}V\n({name})',
                fontsize=9, color='red', fontweight='bold')

    ax.set_xlabel('Circuit Position', fontsize=12)
    ax.set_ylabel('Electric Potential (V)', fontsize=12)
    ax.set_title(f'Potential Distribution in Series Circuit (Ra={Ra}Ω, Rb={Rb}Ω, Rc={Rc}Ω)',
                fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(labels_x, fontsize=8)
    ax.axhline(y=0, color='gray', linestyle='--', linewidth=0.8)
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(alpha=0.3)

    # Summary box
    summary = (f'I = {I*1000:.3f} mA\n'
               f'Va = {Va:.3f} V\nVb = {Vb:.3f} V\nVc = {Vc:.3f} V\n'
               f'ΣV = {Va+Vb+Vc:.3f} V = V_PS ✓')
    ax.text(0.02, 0.6, summary, transform=ax.transAxes, fontsize=9,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    plt.tight_layout()
    return fig


def generate_full_pdf(filename, set_label, Ra, Rb, Rc):
    V_ps = 10.0
    with PdfPages(filename) as pdf:
        # Page 1: Title + Series Req circuit
        fig = draw_series_req_circuit(Ra, Rb, Rc,
            f'{set_label} — Fig 1.1: Series Connection (Req Measurement)')
        pdf.savefig(fig)
        plt.close(fig)

        # Page 2: Series circuit with power supply
        fig = draw_series_circuit_simple(Ra, Rb, Rc,
            f'{set_label} — Fig 1.2: Series Circuit (V_PS = 10V)')
        pdf.savefig(fig)
        plt.close(fig)

        # Page 3: Potential distribution in series
        fig = draw_potential_map_series(Ra, Rb, Rc, V_ps)
        pdf.savefig(fig)
        plt.close(fig)

        # Page 4: Series voltage analysis
        fig = draw_voltage_distribution_series(Ra, Rb, Rc, V_ps)
        pdf.savefig(fig)
        plt.close(fig)

        # Page 5: Parallel Req circuit
        fig = draw_parallel_req_circuit(Ra, Rb, Rc,
            f'{set_label} — Fig 2.1: Parallel Connection (Req Measurement)')
        pdf.savefig(fig)
        plt.close(fig)

        # Page 6: Parallel circuit with power supply
        fig = draw_parallel_circuit_simple(Ra, Rb, Rc,
            f'{set_label} — Fig 2.2: Parallel Circuit (V_PS = 10V)')
        pdf.savefig(fig)
        plt.close(fig)

        # Page 7: Current distribution in parallel
        fig = draw_current_distribution_parallel(Ra, Rb, Rc, V_ps)
        pdf.savefig(fig)
        plt.close(fig)

    print(f'Created {filename}')


# Generate for both sets
generate_full_pdf(r'd:\Sem2_Vizja\electronics\solve1_circuits.pdf', 'Set 1 (Ra=1kΩ, Rb=2kΩ, Rc=3kΩ)', 1000, 2000, 3000)
generate_full_pdf(r'd:\Sem2_Vizja\electronics\solve2_circuits.pdf', 'Set 2 (Ra=1kΩ, Rb=3kΩ, Rc=5kΩ)', 1000, 3000, 5000)
