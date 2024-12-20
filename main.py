import pytest
import allure
from setup import driver_setup as ds
from tests import test_money_transfer_picash, test_picash_recharge, test_accept_driver_services, test_driver_register, test_bicitaxi_request, test_grua_request, test_chat_central, test_add_new_vehicle, service_moto_request, service_motovip_request, signup, service_pibox_request, programed_service_moto, test_login
from tests.e2e import bike_request_flow

# Función principal, no para pytest, solo para ejecución manual
def main():
    # Inicializar el driver
    driver = ds.init_driver()

    # Ejecutar el proceso de login manualmente
    # test_login.test_login_flow(driver)
    # Ejecutar otros procesos comentados si es necesario
    # test_login.main(driver)
    # signup.main(driver)
    # service_moto_request.booking_request(driver)
    # service_motovip_request.booking_request(driver)
    # service_pibox_request.main(driver)
    # programed_service_moto.booking_request(driver)
    # test_add_new_vehicle.addNewVehicle(driver)
    # test_chat_central.main(driver)
    # test_grua_request.gura_request(driver)
    # test_bicitaxi_request.main(driver)
    # test_driver_register.main(driver)
    # test_accept_driver_services.main(driver)
    # test_picash_recharge.main(driver)
    # test_money_transfer_picash.main(driver)
    
    # Pruebas e2e
    bike_request_flow.e2e_login_and_service_flow(driver)

    # Finalizar el driver
    # driver.quit()

# Esto solo se ejecuta cuando se corre manualmente
if __name__ == "__main__":
    main()