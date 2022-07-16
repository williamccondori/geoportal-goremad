export { default as NuxtLogo } from '../../components/NuxtLogo.vue'
export { default as Tutorial } from '../../components/Tutorial.vue'
export { default as LoginForm } from '../../components/login/LoginForm.vue'
export { default as RasterlayerRasterLayerForm } from '../../components/rasterlayer/RasterLayerForm.vue'
export { default as RasterlayerRasterLayerTable } from '../../components/rasterlayer/RasterLayerTable.vue'
export { default as SharedPage } from '../../components/shared/Page.vue'
export { default as VectorlayerVectorLayerForm } from '../../components/vectorlayer/VectorLayerForm.vue'
export { default as VectorlayerVectorLayerTable } from '../../components/vectorlayer/VectorLayerTable.vue'

// nuxt/nuxt.js#8607
function wrapFunctional(options) {
  if (!options || !options.functional) {
    return options
  }

  const propKeys = Array.isArray(options.props) ? options.props : Object.keys(options.props || {})

  return {
    render(h) {
      const attrs = {}
      const props = {}

      for (const key in this.$attrs) {
        if (propKeys.includes(key)) {
          props[key] = this.$attrs[key]
        } else {
          attrs[key] = this.$attrs[key]
        }
      }

      return h(options, {
        on: this.$listeners,
        attrs,
        props,
        scopedSlots: this.$scopedSlots,
      }, this.$slots.default)
    }
  }
}
