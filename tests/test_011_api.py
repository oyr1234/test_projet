import pytest
import requests
from utilities.readProperties import ReadConfig
from utilities.newCustomLogger import LogGen
from time import time
import pytest_assume

@pytest.mark.api
class Test_011_API:
    """Tests API complets - Tous les endpoints Swagger v1.0 OAS 3.0"""
    
    apiBaseURL = ReadConfig.getAPIBaseURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen("./Logs/api.log")
    
    @pytest.fixture(scope="class", autouse=True)
    def auth_session(self):
        """Session authentifiée pour tous les tests"""
        self.logger.log_info("🔐 Initialisation session authentifiée")
        login_url = f"{self.apiBaseURL}/Account/login"
        payload = {"username": self.username, "password": self.password}
        
        session = requests.Session()
        try:
            response = session.post(login_url, json=payload, timeout=10)
            if response.status_code == 200:
                # Extraction token JWT
                token = None
                auth_header = response.headers.get('Authorization')
                if auth_header and 'Bearer' in auth_header:
                    token = auth_header.split('Bearer ')[1]
                elif response.json().get('token'):
                    token = response.json()['token']
                
                if token:
                    session.headers['Authorization'] = f'Bearer {token}'
                    self.logger.log_info("✅ Token JWT configuré")
                else:
                    self.logger.log_warning("⚠️ Token non trouvé")
            else:
                self.logger.log_warning(f"⚠️ Login: {response.status_code}")
        except Exception as e:
            self.logger.log_error(f"❌ Auth: {str(e)}")
        
        yield session
        self.logger.log_info("🔓 Session fermée")

    # ============= ACCOUNT =============
    
    @pytest.mark.P0
    def test_TC061_api_post_login(self):
        """TC-061: POST /api/Account/login"""
        self.logger.log_info("========== TC-061: POST /api/Account/login ==========")
        url = f"{self.apiBaseURL}/Account/login"
        payload = {"username": self.username, "password": self.password}
        
        response = requests.post(url, json=payload, timeout=10)
        self.logger.log_info(f"Status: {response.status_code}")
        pytest_assume.assume(response.status_code == 200, "Login failed")

    @pytest.mark.P1
    def test_TC_account_register(self):
        """TC-Account-Register: POST /api/Account/register"""
        self.logger.log_info("========== TC-Account-Register ==========")
        url = f"{self.apiBaseURL}/Account/register"
        payload = {
            "username": f"testuser{int(time())}",
            "email": f"test{int(time())}@test.com",
            "password": "Pass123!"
        }
        
        response = requests.post(url, json=payload, timeout=10)
        self.logger.log_info(f"Status: {response.status_code}")
        pytest_assume.assume(response.status_code in [200, 201], "Register failed")

    # ============= PATIENTS =============
    
    @pytest.mark.P0
    def test_TC062_api_get_patients(self, auth_session):
        """TC-062: GET /api/Patients"""
        self.logger.log_info("========== TC-062: GET /api/Patients ==========")
        url = f"{self.apiBaseURL}/Patients"
        
        response = auth_session.get(url, timeout=10)
        pytest_assume.assume(response.status_code == 200, "GET Patients failed")
        data = response.json()
        self.logger.log_info(f"PASSED: {len(data)} patients")

    @pytest.mark.P0
    def test_TC063_api_post_patients(self, auth_session):
        """TC-063: POST /api/Patients"""
        self.logger.log_info("========== TC-063: POST /api/Patients ==========")
        url = f"{self.apiBaseURL}/Patients"
        ts = int(time())
        payload = {
            "nom": "TestPatient",
            "prenom": "API",
            "cin": f"88{ts:06d}",
            "adresse": "API Test Address",
            "dateNaissance": "1990-01-01"
        }
        
        response = auth_session.post(url, json=payload, timeout=10)
        pytest_assume.assume(response.status_code in [200, 201], "POST Patient failed")
        self.logger.log_info("PASSED")

    @pytest.mark.P1
    def test_TC_patients_get_by_id(self, auth_session):
        """TC-Patients-GetById: GET /api/Patients/{id}"""
        self.logger.log_info("========== TC-Patients-GetById ==========")
        url = f"{self.apiBaseURL}/Patients/1"
        
        response = auth_session.get(url, timeout=10)
        pytest_assume.assume(response.status_code in [200, 404], "GET Patient/{id} failed")

    @pytest.mark.P1
    def test_TC_patients_count(self, auth_session):
        """TC-Patients-Count: GET /api/Patients/count"""
        self.logger.log_info("========== TC-Patients-Count ==========")
        url = f"{self.apiBaseURL}/Patients/count"
        
        response = auth_session.get(url, timeout=10)
        pytest_assume.assume(response.status_code == 200, "Patients count failed")

    @pytest.mark.P1
    def test_TC_patients_put(self, auth_session):
        """TC-Patients-Update: PUT /api/Patients"""
        self.logger.log_info("========== TC-Patients-Update ==========")
        url = f"{self.apiBaseURL}/Patients"
        payload = {"patientId": 1, "nom": "Updated", "prenom": "Patient"}
        
        response = auth_session.put(url, json=payload, timeout=10)
        pytest_assume.assume(response.status_code in [200, 204], "PUT Patient failed")

    @pytest.mark.P1
    def test_TC_patients_delete(self, auth_session):
        """TC-Patients-Delete: DELETE /api/Patients/{id}"""
        self.logger.log_info("========== TC-Patients-Delete ==========")
        url = f"{self.apiBaseURL}/Patients/999"
        
        response = auth_session.delete(url, timeout=10)
        pytest_assume.assume(response.status_code in [200, 204, 404], "DELETE Patient failed")

    # ============= MEDECINS =============
    
    @pytest.mark.P0
    def test_TC064_api_get_medecins(self, auth_session):
        """TC-064: GET /api/Medecins"""
        self.logger.log_info("========== TC-064: GET /api/Medecins ==========")
        url = f"{self.apiBaseURL}/Medecins"
        
        response = auth_session.get(url, timeout=10)
        pytest_assume.assume(response.status_code == 200, "GET Medecins failed")
        data = response.json()
        self.logger.log_info(f"PASSED: {len(data)} médecins")

    @pytest.mark.P1
    def test_TC_medecins_post(self, auth_session):
        """TC-Medecins-Create: POST /api/Medecins"""
        self.logger.log_info("========== TC-Medecins-Create ==========")
        url = f"{self.apiBaseURL}/Medecins"
        payload = {
            "nom": "MedecinTest",
            "prenom": "API",
            "numeroProfessionnel": f"MED{int(time())}",
            "specialite": "Cardiologie",
            "telephone": "9876543210"
        }
        
        response = auth_session.post(url, json=payload, timeout=10)
        pytest_assume.assume(response.status_code in [200, 201], "POST Medecin failed")

    @pytest.mark.P1
    def test_TC_medecins_get_by_id(self, auth_session):
        """TC-Medecins-GetById"""
        self.logger.log_info("========== TC-Medecins-GetById ==========")
        url = f"{self.apiBaseURL}/Medecins/1"
        response = auth_session.get(url, timeout=10)
        pytest_assume.assume(response.status_code in [200, 404])

    @pytest.mark.P1
    def test_TC_medecins_put(self, auth_session):
        """TC-Medecins-Update"""
        self.logger.log_info("========== TC-Medecins-Update ==========")
        url = f"{self.apiBaseURL}/Medecins"
        payload = {"medecinId": 1, "nom": "UpdatedMedecin", "specialite": "Neurologie"}
        response = auth_session.put(url, json=payload, timeout=10)
        pytest_assume.assume(response.status_code in [200, 204])

    @pytest.mark.P1
    def test_TC_medecins_delete(self, auth_session):
        """TC-Medecins-Delete"""
        self.logger.log_info("========== TC-Medecins-Delete ==========")
        url = f"{self.apiBaseURL}/Medecins/999"
        response = auth_session.delete(url, timeout=10)
        pytest_assume.assume(response.status_code in [200, 204, 404])

    # ============= MEDICAMENTS =============
    
    @pytest.mark.P0
    def test_TC065_api_get_medicaments(self, auth_session):
        """TC-065: GET /api/Medicaments"""
        self.logger.log_info("========== TC-065: GET /api/Medicaments ==========")
        url = f"{self.apiBaseURL}/Medicaments"
        
        response = auth_session.get(url, timeout=10)
        pytest_assume.assume(response.status_code == 200)
        data = response.json()
        self.logger.log_info(f"PASSED: {len(data)} médicaments")

    @pytest.mark.P1
    def test_TC_medicaments_post(self, auth_session):
        """TC-Medicaments-Create"""
        self.logger.log_info("========== TC-Medicaments-Create ==========")
        url = f"{self.apiBaseURL}/Medicaments"
        payload = {
            "nom": "Paracétamol Test",
            "description": "Analgésique",
            "dosage": "500mg",
            "forme": "Comprimé",
            "prix": 5.99
        }
        
        response = auth_session.post(url, json=payload, timeout=10)
        pytest_assume.assume(response.status_code in [200, 201])

    @pytest.mark.P1
    def test_TC_medicaments_get_by_id(self, auth_session):
        """TC-Medicaments-GetById"""
        self.logger.log_info("========== TC-Medicaments-GetById ==========")
        url = f"{self.apiBaseURL}/Medicaments/1"
        response = auth_session.get(url, timeout=10)
        pytest_assume.assume(response.status_code in [200, 404])

    @pytest.mark.P1
    def test_TC_medicaments_put(self, auth_session):
        """TC-Medicaments-Update"""
        self.logger.log_info("========== TC-Medicaments-Update ==========")
        url = f"{self.apiBaseURL}/Medicaments"
        payload = {"medicamentId": 1, "nom": "Updated Medicament", "prix": 7.99}
        response = auth_session.put(url, json=payload, timeout=10)
        pytest_assume.assume(response.status_code in [200, 204])

    @pytest.mark.P1
    def test_TC_medicaments_delete(self, auth_session):
        """TC-Medicaments-Delete"""
        self.logger.log_info("========== TC-Medicaments-Delete ==========")
        url = f"{self.apiBaseURL}/Medicaments/999"
        response = auth_session.delete(url, timeout=10)
        pytest_assume.assume(response.status_code in [200, 204, 404])

    # ============= ORDONNANCES =============
    
    @pytest.mark.P0
    def test_TC066_api_get_ordonnances(self, auth_session):
        """TC-066: GET /api/Ordonnances"""
        self.logger.log_info("========== TC-066: GET /api/Ordonnances ==========")
        url = f"{self.apiBaseURL}/Ordonnances"
        
        response = auth_session.get(url, timeout=10)
        pytest_assume.assume(response.status_code == 200)
        data = response.json()
        self.logger.log_info(f"PASSED: {len(data)} ordonnances")

    @pytest.mark.P0
    def test_TC067_api_post_ordonnances(self, auth_session):
        """TC-067: POST /api/Ordonnances"""
        self.logger.log_info("========== TC-067: POST /api/Ordonnances ==========")
        url = f"{self.apiBaseURL}/Ordonnances"
        payload = {
            "dateOrdonnance": "2026-01-19",
            "patientId": 1,
            "pharmacienId": 1,
            "medecinId": 1,
            "commentaire": "Test API Ordonnance"
        }
        
        response = auth_session.post(url, json=payload, timeout=10)
        pytest_assume.assume(response.status_code in [200, 201])

    @pytest.mark.P1
    def test_TC_ordonnances_get_by_id(self, auth_session):
        """TC-Ordonnances-GetById"""
        self.logger.log_info("========== TC-Ordonnances-GetById ==========")
        url = f"{self.apiBaseURL}/Ordonnances/1"
        response = auth_session.get(url, timeout=10)
        pytest_assume.assume(response.status_code in [200, 404])

    @pytest.mark.P1
    def test_TC_ordonnances_by_pharmacien(self, auth_session):
        """TC-Ordonnances-ByPharmacien"""
        self.logger.log_info("========== TC-Ordonnances-ByPharmacien ==========")
        url = f"{self.apiBaseURL}/Ordonnances/by-pharmacien"
        response = auth_session.get(url, timeout=10)
        pytest_assume.assume(response.status_code == 200)

    @pytest.mark.P1
    def test_TC_ordonnances_put(self, auth_session):
        """TC-Ordonnances-Update"""
        self.logger.log_info("========== TC-Ordonnances-Update ==========")
        url = f"{self.apiBaseURL}/Ordonnances"
        payload = {"ordonnanceId": 1, "commentaire": "Updated Commentaire"}
        response = auth_session.put(url, json=payload, timeout=10)
        pytest_assume.assume(response.status_code in [200, 204])

    @pytest.mark.P1
    def test_TC_ordonnances_delete(self, auth_session):
        """TC-Ordonnances-Delete"""
        self.logger.log_info("========== TC-Ordonnances-Delete ==========")
        url = f"{self.apiBaseURL}/Ordonnances/999"
        response = auth_session.delete(url, timeout=10)
        pytest_assume.assume(response.status_code in [200, 204, 404])

    # ============= PHARMACIENS =============
    
    @pytest.mark.P1
    def test_TC_pharmaciens_get(self, auth_session):
        """TC-Pharmaciens-Get"""
        self.logger.log_info("========== TC-Pharmaciens-Get ==========")
        url = f"{self.apiBaseURL}/Pharmaciens"
        response = auth_session.get(url, timeout=10)
        pytest_assume.assume(response.status_code == 200)

    @pytest.mark.P1
    def test_TC_pharmaciens_post(self, auth_session):
        """TC-Pharmaciens-Create"""
        self.logger.log_info("========== TC-Pharmaciens-Create ==========")
        url = f"{self.apiBaseURL}/Pharmaciens"
        ts = int(time())
        payload = {
            "nom": "PharmacienTest",
            "prenom": "API",
            "email": f"pharm{ts}@test.com",
            "telephone": "9876543210",
            "numeroInscription": f"PHARM{ts}",
            "pharmacieId": 1
        }
        response = auth_session.post(url, json=payload, timeout=10)
        pytest_assume.assume(response.status_code in [200, 201])

    @pytest.mark.P1
    def test_TC_pharmaciens_get_by_id(self, auth_session):
        """TC-Pharmaciens-GetById"""
        self.logger.log_info("========== TC-Pharmaciens-GetById ==========")
        url = f"{self.apiBaseURL}/Pharmaciens/1"
        response = auth_session.get(url, timeout=10)
        pytest_assume.assume(response.status_code in [200, 404])

    @pytest.mark.P1
    def test_TC_pharmaciens_me(self, auth_session):
        """TC-Pharmaciens-Me"""
        self.logger.log_info("========== TC-Pharmaciens-Me ==========")
        url = f"{self.apiBaseURL}/Pharmaciens/me"
        response = auth_session.get(url, timeout=10)
        pytest_assume.assume(response.status_code in [200, 401])

    @pytest.mark.P1
    def test_TC_pharmaciens_put(self, auth_session):
        """TC-Pharmaciens-Update"""
        self.logger.log_info("========== TC-Pharmaciens-Update ==========")
        url = f"{self.apiBaseURL}/Pharmaciens"
        payload = {"pharmacienId": 1, "nom": "UpdatedPharmacien"}
        response = auth_session.put(url, json=payload, timeout=10)
        pytest_assume.assume(response.status_code in [200, 204])

    @pytest.mark.P1
    def test_TC_pharmaciens_delete(self, auth_session):
        """TC-Pharmaciens-Delete"""
        self.logger.log_info("========== TC-Pharmaciens-Delete ==========")
        url = f"{self.apiBaseURL}/Pharmaciens/999"
        response = auth_session.delete(url, timeout=10)
        pytest_assume.assume(response.status_code in [200, 204, 404])

    # ============= PHARMACIES =============
    
    @pytest.mark.P1
    def test_TC_pharmacies_get(self, auth_session):
        """TC-Pharmacies-Get"""
        self.logger.log_info("========== TC-Pharmacies-Get ==========")
        url = f"{self.apiBaseURL}/Pharmacies"
        response = auth_session.get(url, timeout=10)
        pytest_assume.assume(response.status_code == 200)

    @pytest.mark.P1
    def test_TC_pharmacies_post(self, auth_session):
        """TC-Pharmacies-Create"""
        self.logger.log_info("========== TC-Pharmacies-Create ==========")
        url = f"{self.apiBaseURL}/Pharmacies"
        payload = {
            "nom": f"PharmacieTest{int(time())}",
            "adresse": "Test Address Sfax",
            "telephone": "9876543210"
        }
        response = auth_session.post(url, json=payload, timeout=10)
        pytest_assume.assume(response.status_code in [200, 201])

    @pytest.mark.P1
    def test_TC_pharmacies_get_by_id(self, auth_session):
        """TC-Pharmacies-GetById"""
        self.logger.log_info("========== TC-Pharmacies-GetById ==========")
        url = f"{self.apiBaseURL}/Pharmacies/1"
        response = auth_session.get(url, timeout=10)
        pytest_assume.assume(response.status_code in [200, 404])

    @pytest.mark.P1
    def test_TC_pharmacies_put(self, auth_session):
        """TC-Pharmacies-Update"""
        self.logger.log_info("========== TC-Pharmacies-Update ==========")
        url = f"{self.apiBaseURL}/Pharmacies"
        payload = {"pharmacieId": 1, "nom": "Updated Pharmacy"}
        response = auth_session.put(url, json=payload, timeout=10)
        pytest_assume.assume(response.status_code in [200, 204])

    @pytest.mark.P1
    def test_TC_pharmacies_delete(self, auth_session):
        """TC-Pharmacies-Delete"""
        self.logger.log_info("========== TC-Pharmacies-Delete ==========")
        url = f"{self.apiBaseURL}/Pharmacies/999"
        response = auth_session.delete(url, timeout=10)
        pytest_assume.assume(response.status_code in [200, 204, 404])

    # ============= STOCKS MEDICAMENTS =============
    
    @pytest.mark.P1
    def test_TC_stocks_get(self, auth_session):
        """TC-Stocks-Get"""
        self.logger.log_info("========== TC-Stocks-Get ==========")
        url = f"{self.apiBaseURL}/StocksMedicaments"
        response = auth_session.get(url, timeout=10)
        pytest_assume.assume(response.status_code == 200)

    @pytest.mark.P1
    def test_TC_stocks_post(self, auth_session):
        """TC-Stocks-Create"""
        self.logger.log_info("========== TC-Stocks-Create ==========")
        url = f"{self.apiBaseURL}/StocksMedicaments"
        payload = {
            "medicamentId": 1,
            "pharmacieId": 1,
            "quantite": 100,
            "prixUnitaire": 5.99,
            "datePeremption": "2027-01-19"
        }
        response = auth_session.post(url, json=payload, timeout=10)
        pytest_assume.assume(response.status_code in [200, 201])

    @pytest.mark.P1
    def test_TC_stocks_get_by_pharmacie(self, auth_session):
        """TC-Stocks-ByPharmacie"""
        self.logger.log_info("========== TC-Stocks-ByPharmacie ==========")
        url = f"{self.apiBaseURL}/StocksMedicaments/by-pharmacie/1"
        response = auth_session.get(url, timeout=10)
        pytest_assume.assume(response.status_code == 200)

    @pytest.mark.P1
    def test_TC_stocks_put(self, auth_session):
        """TC-Stocks-Update"""
        self.logger.log_info("========== TC-Stocks-Update ==========")
        url = f"{self.apiBaseURL}/StocksMedicaments"
        payload = {"stockMedicamentId": 1, "quantite": 150}
        response = auth_session.put(url, json=payload, timeout=10)
        pytest_assume.assume(response.status_code in [200, 204])

    @pytest.mark.P1
    def test_TC_stocks_delete(self, auth_session):
        """TC-Stocks-Delete"""
        self.logger.log_info("========== TC-Stocks-Delete ==========")
        url = f"{self.apiBaseURL}/StocksMedicaments/999"
        response = auth_session.delete(url, timeout=10)
        pytest_assume.assume(response.status_code in [200, 204, 404])

    # ============= ENDPOINTS COMPLEMENTAIRES =============
    
    @pytest.mark.P1
    def test_TC_historiques_medicaments(self, auth_session):
        """TC-HistoriquesMedicaments"""
        self.logger.log_info("========== TC-HistoriquesMedicaments ==========")
        url = f"{self.apiBaseURL}/HistoriquesMedicaments"
        response = auth_session.get(url, timeout=10)
        pytest_assume.assume(response.status_code == 200)

    @pytest.mark.P1
    def test_TC_lignes_ordonnance(self, auth_session):
        """TC-LignesOrdonnance"""
        self.logger.log_info("========== TC-LignesOrdonnance ==========")
        url = f"{self.apiBaseURL}/LignesOrdonnance"
        response = auth_session.get(url, timeout=10)
        pytest_assume.assume(response.status_code == 200)

    @pytest.mark.P1
    def test_TC_suivis_ordonnance(self, auth_session):
        """TC-SuivisOrdonnance"""
        self.logger.log_info("========== TC-SuivisOrdonnance ==========")
        url = f"{self.apiBaseURL}/SuivisOrdonnance"
        response = auth_session.get(url, timeout=10)
        pytest_assume.assume(response.status_code == 200)

    @pytest.mark.P1
    def test_TC_weather_forecast(self, auth_session):
        """TC-WeatherForecast (Sample)"""
        self.logger.log_info("========== TC-WeatherForecast ==========")
        url = f"{self.apiBaseURL}/WeatherForecast"
        response = auth_session.get(url, timeout=10)
        pytest_assume.assume(response.status_code == 200)
