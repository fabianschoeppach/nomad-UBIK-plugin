from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class MySchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_uibk_plugin.schema_packages.mypackage import m_package

        return m_package


mypackage = MySchemaPackageEntryPoint(
    name='MyPackage',
    description='Schema package defined using the new plugin mechanism.',
)


class XRFSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from nomad_uibk_plugin.schema_packages.XRFschema import m_package

        return m_package


xrfschema = XRFSchemaPackageEntryPoint(
    name='XRFSchema',
    description='XRF Schema package defined using the new plugin mechanism.',
)


class MicroCellSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from nomad_uibk_plugin.schema_packages.microcellschema import m_package

        return m_package


microcellschema = MicroCellSchemaPackageEntryPoint(
    name='MicroCellSchema',
    description='MicroCell Schema package defined using the new plugin mechanism.',
)
