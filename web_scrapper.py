import requests
import json
from web_page_scrapper import WebScrapper
url = "https://5vcn8neb3h-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(3.33.0)%3B%20Browser%20(lite)%3B%20react%20(16.8.6)%3B%20react-instantsearch%20(5.6.0)%3B%20JS%20Helper%20(2.28.0)&x-algolia-application-id=5VCN8NEB3H&x-algolia-api-key=458f2fcfb20def090c810b3a47b86f2a"
stringFormat = '{"requests":[{"indexName":"resin","params":"query=&hitsPerPage=15&maxValuesPerFacet=25&page=0&highlightPreTag=%3Cais-highlight-0000000000%3E&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&facets=%5B%22productInformation.matrixType%22%2C%22productInformation.resinType%22%2C%22productInformation.productFormat%22%2C%22generalProperties.density_metric%22%2C%22generalProperties.moisture%22%2C%22generalProperties.outGassing_TML%22%2C%22generalProperties.outGassing_CVCM%22%2C%22generalProperties.outGassing_WVR%22%2C%22generalProperties.tackLife%22%2C%22generalProperties.outLife%22%2C%22generalProperties.shelfLife%22%2C%22generalProperties.waterAbsorption%22%2C%22generalProperties.humidityAbsorption%22%2C%22generalProperties.toughened%22%2C%22generalProperties.flameRetardant%22%2C%22generalProperties.burningBehavior%22%2C%22processingProperties.transformationProcess%22%2C%22processingProperties.curingProcess%22%2C%22processingProperties.cureTemp_C%22%2C%22processingProperties.cureTime%22%2C%22processingProperties.gelTime%22%2C%22processingProperties.gelTemp_C%22%2C%22processingProperties.minVisco_metric%22%2C%22processingProperties.minViscoTemp_C%22%2C%22processingProperties.mixVisco_metric%22%2C%22processingProperties.mixViscoTemp_C%22%2C%22processingProperties.potLife%22%2C%22processingProperties.meltVolumeFlowRate_metric%22%2C%22processingProperties.meltMassFlowRate_metric%22%2C%22processingProperties.meltFlowTemperature_C%22%2C%22processingProperties.meltFlowLoad_metric%22%2C%22processingProperties.dryingTemperature_C%22%2C%22processingProperties.dryingTime%22%2C%22processingProperties.meltTemperature_C%22%2C%22processingProperties.moldTemperature_C%22%2C%22processingProperties.mouldingShrinkageParallel%22%2C%22processingProperties.mouldingShrinkageNormal%22%2C%22mechanicalProperties.tensileStrength_metric%22%2C%22mechanicalProperties.tensileModulus_metric%22%2C%22mechanicalProperties.tensileStrain%22%2C%22mechanicalProperties.tensileYieldStrength_metric%22%2C%22mechanicalProperties.tensileYieldStrain%22%2C%22mechanicalProperties.flexuralStrength_metric%22%2C%22mechanicalProperties.flexuralModulus_metric%22%2C%22mechanicalProperties.compressionStrength_metric%22%2C%22mechanicalProperties.compressionModulus_metric%22%2C%22mechanicalProperties.ilss_metric%22%2C%22mechanicalProperties.k1c_metric%22%2C%22mechanicalProperties.g1c_metric%22%2C%22mechanicalProperties.charpyImpactStrength23%22%2C%22mechanicalProperties.charpyImpactStrengthMinus30%22%2C%22mechanicalProperties.charpyNotchedImpactStrength23%22%2C%22mechanicalProperties.charpyNotchedImpactStrengthMinus30%22%2C%22thermalProperties.thermalConductivity_metric%22%2C%22thermalProperties.coeffThermalExpansion_metric%22%2C%22thermalProperties.coeffThermalExpansionParallel%22%2C%22thermalProperties.coeffThermalExpansionNormal%22%2C%22thermalProperties.tg_C%22%2C%22thermalProperties.tgOnDry_C%22%2C%22thermalProperties.tgPeakDry_C%22%2C%22thermalProperties.tgOnWet_C%22%2C%22thermalProperties.tgPeakWet_C%22%2C%22thermalProperties.tgPC_C%22%2C%22thermalProperties.meltTemp_C%22%2C%22thermalProperties.serviceTemp_C%22%2C%22thermalProperties.tempDeflection18_C%22%2C%22thermalProperties.tempDeflection045_C%22%2C%22electricalProperties.lossTangent%22%2C%22electricalProperties.dielectricConstant%22%2C%22electricalProperties.electricStrength_metric%22%2C%22electricalProperties.volumeResistivity%22%2C%22electricalProperties.surfaceResistivity%22%2C%22electricalProperties.relativePermittivity%22%2C%22electricalProperties.dissipationFactor%22%2C%22electricalProperties.comparativeTrackingIndex%22%2C%22moreProperties.prepregUse%22%2C%22moreProperties.use%22%5D&tagFilters=&facetFilters=%5B%5B%22productInformation.resinType%3ABMI%22%5D%2C%5B%22productInformation.matrixType%3AThermoset%22%5D%5D"},{"indexName":"resin","params":"query=&hitsPerPage=1&maxValuesPerFacet=25&page=0&highlightPreTag=%3Cais-highlight-0000000000%3E&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&attributesToRetrieve=%5B%5D&attributesToHighlight=%5B%5D&attributesToSnippet=%5B%5D&tagFilters=&analytics=false&clickAnalytics=false&facets=productInformation.resinType&facetFilters=%5B%5B%22productInformation.matrixType%3AThermoset%22%5D%5D"},{"indexName":"resin","params":"query=&hitsPerPage=1&maxValuesPerFacet=25&page=0&highlightPreTag=%3Cais-highlight-0000000000%3E&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&attributesToRetrieve=%5B%5D&attributesToHighlight=%5B%5D&attributesToSnippet=%5B%5D&tagFilters=&analytics=false&clickAnalytics=false&facets=productInformation.matrixType&facetFilters=%5B%5B%22productInformation.resinType%3ABMI%22%5D%5D"}]}'


def save_to_file(elements):
    pretty_json = json.dumps(elements, indent=4, sort_keys=True)
    with open("data.txt", "w") as file:
        file.write(str(pretty_json))

def start_scraping(data):
    web_scrapper = WebScrapper()
    formatted_data = json.loads(data)
    results = formatted_data['results']
    first_element = results[0]
    hits = first_element['hits']
    save_to_file(hits)
    final_result = []
    for element in hits:
        final_result.append(web_scrapper.request_data(element['unique_product_id']))
    save_to_file(final_result)



response = requests.post(url, stringFormat)
start_scraping(response.text)

