# state file generated using paraview version 5.9.0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [868, 673]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.000666450709104538, 9.313225746154785e-09, 0.001049774291459471]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.000666450709104538, 9.313225746154785e-09, 0.11408991966543003]
renderView1.CameraFocalPoint = [0.000666450709104538, 9.313225746154785e-09, 0.001049774291459471]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.042835089490738304
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitle = 'X '
renderView1.AxesGrid.YTitle = 'Y'
renderView1.AxesGrid.ZTitle = 'Z'
renderView1.AxesGrid.XTitleFontFamily = 'Times'
renderView1.AxesGrid.XTitleFontSize = 17
renderView1.AxesGrid.YTitleFontFamily = 'Times'
renderView1.AxesGrid.YTitleFontSize = 17
renderView1.AxesGrid.ZTitleFontFamily = 'Times'
renderView1.AxesGrid.ZTitleFontSize = 17
renderView1.AxesGrid.FacesToRender = 32
renderView1.AxesGrid.CullBackface = 1
renderView1.AxesGrid.CullFrontface = 0
renderView1.AxesGrid.ShowTicks = 0
renderView1.AxesGrid.AxesToLabel = 0
renderView1.AxesGrid.LabelUniqueEdgesOnly = 0
renderView1.AxesGrid.XLabelFontFamily = 'Times'
renderView1.AxesGrid.XLabelFontSize = 20
renderView1.AxesGrid.YLabelFontFamily = 'Times'
renderView1.AxesGrid.YLabelFontSize = 20
renderView1.AxesGrid.ZLabelFontFamily = 'Times'
renderView1.AxesGrid.ZLabelFontSize = 20
renderView1.AxesGrid.XAxisPrecision = 0
renderView1.AxesGrid.YAxisPrecision = 0

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(868, 673)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Legacy VTK Reader'
p = LegacyVTKReader(registrationName='p*', FileNames=['/home/akhil/Documents/wave/hcp_liggghts/point_defect/chain2/xdirec/ak/p6750000.vtk'])

# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=p,
    GlyphType='Line')
glyph1.OrientationArray = ['CELLS', 'force_normal']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.VectorScaleMode = 'Scale by Components'
glyph1.ScaleFactor = 0.002
glyph1.GlyphTransform = 'Transform2'
glyph1.GlyphMode = 'All Points'

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=glyph1)
calculator1.ResultArrayName = 'Normalized force'
calculator1.Function = 'force_normal/510'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from p
pDisplay = Show(p, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'force_normal'
force_normalLUT = GetColorTransferFunction('force_normal')
force_normalLUT.RGBPoints = [0.0, 1.0, 1.0, 1.0, 86.7, 0.0, 0.0, 1.0, 173.40000000000003, 0.0, 1.0, 1.0, 255.0, 0.0, 1.0, 0.0, 341.70000000000005, 1.0, 1.0, 0.0, 428.4, 1.0, 0.0, 0.0, 510.0, 0.878431372549, 0.0, 1.0]
force_normalLUT.ColorSpace = 'RGB'
force_normalLUT.NanColor = [1.0, 0.0, 0.0]
force_normalLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
pDisplay.Representation = 'Surface'
pDisplay.ColorArrayName = ['CELLS', 'force_normal']
pDisplay.LookupTable = force_normalLUT
pDisplay.PointSize = 0.5
pDisplay.LineWidth = 3.0
pDisplay.SelectTCoordArray = 'None'
pDisplay.SelectNormalArray = 'None'
pDisplay.SelectTangentArray = 'None'
pDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
pDisplay.SelectOrientationVectors = 'None'
pDisplay.ScaleFactor = 0.007785080000758171
pDisplay.SelectScaleArray = 'None'
pDisplay.GlyphType = 'Arrow'
pDisplay.GlyphTableIndexArray = 'None'
pDisplay.GaussianRadius = 0.00038925400003790854
pDisplay.SetScaleArray = ['POINTS', '']
pDisplay.ScaleTransferFunction = 'PiecewiseFunction'
pDisplay.OpacityArray = ['POINTS', '']
pDisplay.OpacityTransferFunction = 'PiecewiseFunction'
pDisplay.DataAxesGrid = 'GridAxesRepresentation'
pDisplay.PolarAxes = 'PolarAxesRepresentation'

# show data from glyph1
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'force_normal']
glyph1Display.LookupTable = force_normalLUT
glyph1Display.PointSize = 0.5
glyph1Display.LineWidth = 4.0
glyph1Display.SelectTCoordArray = 'None'
glyph1Display.SelectNormalArray = 'None'
glyph1Display.SelectTangentArray = 'None'
glyph1Display.OSPRayScaleArray = 'contact_area'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'None'
glyph1Display.ScaleFactor = 0.008563587814569474
glyph1Display.SelectScaleArray = 'None'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'None'
glyph1Display.GaussianRadius = 0.00042817939072847366
glyph1Display.SetScaleArray = ['POINTS', '']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', '']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [2.84414e-09, 0.0, 0.5, 0.0, 1.82388e-08, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [2.84414e-09, 0.0, 0.5, 0.0, 1.82388e-08, 1.0, 0.5, 0.0]

# show data from calculator1
calculator1Display = Show(calculator1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'Normalizedforce'
normalizedforceLUT = GetColorTransferFunction('Normalizedforce')
normalizedforceLUT.RGBPoints = [0.0, 1.0, 1.0, 1.0, 0.10000000000000012, 0.85, 0.85, 0.85, 0.20000000000000023, 0.6, 0.8, 1.0, 0.25000000000000033, 0.3, 0.4, 1.0, 0.3000000000000003, 0.3, 0.4, 1.0, 0.35000000000000037, 0.8, 0.6, 1.0, 0.3999999999999999, 0.8, 0.6, 1.0, 0.5, 0.6, 0.3, 1.0, 0.6000000000000001, 0.0, 1.0, 0.0, 0.6999999999999996, 1.0, 0.7, 0.0, 0.8, 1.0, 0.25, 0.0, 0.9, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
normalizedforceLUT.ColorSpace = 'Step'
normalizedforceLUT.NanColor = [0.6509803921568628, 0.3372549019607843, 0.1568627450980392]
normalizedforceLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['POINTS', 'Normalized force']
calculator1Display.LookupTable = normalizedforceLUT
calculator1Display.PointSize = 0.5
calculator1Display.LineWidth = 3.0
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.OSPRayScaleArray = 'contact_area'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'None'
calculator1Display.ScaleFactor = 0.007676109671592712
calculator1Display.SelectScaleArray = 'None'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'None'
calculator1Display.GaussianRadius = 0.0003838054835796356
calculator1Display.SetScaleArray = ['POINTS', 'contact_area']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'contact_area']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [2.18707e-09, 0.0, 0.5, 0.0, 1.4514e-07, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [2.18707e-09, 0.0, 0.5, 0.0, 1.4514e-07, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for force_normalLUT in view renderView1
force_normalLUTColorBar = GetScalarBar(force_normalLUT, renderView1)
force_normalLUTColorBar.AutoOrient = 0
force_normalLUTColorBar.Orientation = 'Horizontal'
force_normalLUTColorBar.WindowLocation = 'UpperRightCorner'
force_normalLUTColorBar.Position = [0.29581626607989175, 0.03940298507462686]
force_normalLUTColorBar.Title = 'Normal Force'
force_normalLUTColorBar.ComponentTitle = ''
force_normalLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
force_normalLUTColorBar.TitleFontFamily = 'Times'
force_normalLUTColorBar.TitleFontSize = 20
force_normalLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
force_normalLUTColorBar.LabelFontFamily = 'Times'
force_normalLUTColorBar.LabelFontSize = 20
force_normalLUTColorBar.UseCustomLabels = 1
force_normalLUTColorBar.CustomLabels = [0.0, 100.0, 200.0, 300.0, 400.0]
force_normalLUTColorBar.AddRangeLabels = 0
force_normalLUTColorBar.DrawAnnotations = 0
force_normalLUTColorBar.ScalarBarThickness = 25
force_normalLUTColorBar.ScalarBarLength = 0.4

# set color bar visibility
force_normalLUTColorBar.Visibility = 0

# get color legend/bar for normalizedforceLUT in view renderView1
normalizedforceLUTColorBar = GetScalarBar(normalizedforceLUT, renderView1)
normalizedforceLUTColorBar.AutoOrient = 0
normalizedforceLUTColorBar.Orientation = 'Horizontal'
normalizedforceLUTColorBar.WindowLocation = 'AnyLocation'
normalizedforceLUTColorBar.Position = [0.19297511032409942, 0.08766716196136702]
normalizedforceLUTColorBar.Title = ''
normalizedforceLUTColorBar.ComponentTitle = ''
normalizedforceLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
normalizedforceLUTColorBar.TitleFontFamily = 'Times'
normalizedforceLUTColorBar.TitleFontSize = 24
normalizedforceLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
normalizedforceLUTColorBar.LabelFontFamily = 'Times'
normalizedforceLUTColorBar.LabelFontSize = 24
normalizedforceLUTColorBar.UseCustomLabels = 1
normalizedforceLUTColorBar.CustomLabels = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
normalizedforceLUTColorBar.AddRangeLabels = 0
normalizedforceLUTColorBar.DrawAnnotations = 0
normalizedforceLUTColorBar.ScalarBarThickness = 18
normalizedforceLUTColorBar.ScalarBarLength = 0.6000000000000006

# set color bar visibility
normalizedforceLUTColorBar.Visibility = 1

# hide data in view
Hide(p, renderView1)

# hide data in view
Hide(glyph1, renderView1)

# show color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'Normalizedforce'
normalizedforcePWF = GetOpacityTransferFunction('Normalizedforce')
normalizedforcePWF.Points = [0.0, 0.0, 0.5, 0.0, 1.0051517084094725, 1.0, 0.5, 0.0]
normalizedforcePWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'force_normal'
force_normalPWF = GetOpacityTransferFunction('force_normal')
force_normalPWF.Points = [0.0, 0.0, 0.5, 0.0, 510.0, 1.0, 0.5, 0.0]
force_normalPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(calculator1)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')
