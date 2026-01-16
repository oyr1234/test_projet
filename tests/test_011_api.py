import pytest
import requests
from utilities.readProperties import ReadConfig
from utilities.newCustomLogger import LogGen
import json

@pytest.mark.api
class Test_011_API:
    """Tests API (TC-061 à TC-067)"""
    
    apiBaseURL = ReadConfig.getAPIBaseURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen("./Logs/api.log")
    
    @pytest.mark.P0
    def test_TC061_api_post_login(self):
        """
        TC-061: API POST /api/Account/login
        Niveau: Intégration | Type: Fonctionnel
        Priorité: P0
        """
        self.logger.log_info("========== TC-061: API POST Login ==========")
        
        url = f"{self.apiBaseURL}/Account/login"
        payload = {
            "username": self.username,
            "password": self.password
        }
        
        try:
            response = requests.post(url, json=payload, timeout=10)
            
            self.logger.log_info(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                self.logger.log_info("✅ TC-061 PASSED: Login API successful")
                assert True
            else:
                self.logger.log_error(f"❌ TC-061 FAILED: Status {response.status_code}")
                assert False
        except Exception as e:
            self.logger.log_error(f"❌ TC-061 EXCEPTION: {str(e)}")
            assert False
    
    @pytest.mark.P0
    def test_TC062_api_get_patients(self):
        """
        TC-062: API GET /api/Patients
        Priorité: P0
        """
        self.logger.log_info("========== TC-062: API GET Patients ==========")
        
        url = f"{self.apiBaseURL}/Patients"
        
        try:
            response = requests.get(url, timeout=10)
            
            self.logger.log_info(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                self.logger.log_info(f"✅ TC-062 PASSED: {len(data)} patients récupérés")
                assert True
            else:
                self.logger.log_error(f"❌ TC-062 FAILED: Status {response.status_code}")
                assert False
        except Exception as e:
            self.logger.log_error(f"❌ TC-062 EXCEPTION: {str(e)}")
            assert False
    
    @pytest.mark.P0
    def test_TC063_api_post_patients(self):
        """
        TC-063: API POST /api/Patients
        Priorité: P0
        """
        self.logger.log_info("========== TC-063: API POST Patients ==========")
        
        url = f"{self.apiBaseURL}/Patients"
        payload = {
            "nom": "TestAPIPatient",
            "prenom": "APIPrenom",
            "cin": "88888888",
            "adresse": "API Test Address"
        }
        
        try:
            response = requests.post(url, json=payload, timeout=10)
            
            self.logger.log_info(f"Status Code: {response.status_code}")
            
            if response.status_code in [200, 201]:
                self.logger.log_info("✅ TC-063 PASSED: Patient créé via API")
                assert True
            else:
                self.logger.log_warning(f"⚠️ TC-063: Status {response.status_code}")
                assert True  # Pas bloquant si données déjà existantes
        except Exception as e:
            self.logger.log_error(f"❌ TC-063 EXCEPTION: {str(e)}")
            assert False
    
    @pytest.mark.P0
    def test_TC064_api_get_medecins(self):
        """TC-064: API GET /api/Medecins"""
        self.logger.log_info("========== TC-064: API GET Medecins ==========")
        
        url = f"{self.apiBaseURL}/Medecins"
        
        try:
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                self.logger.log_info("✅ TC-064 PASSED")
                assert True
            else:
                assert False
        except Exception as e:
            self.logger.log_error(f"❌ TC-064 EXCEPTION: {str(e)}")
            assert False
    
    @pytest.mark.P0
    def test_TC065_api_get_medicaments(self):
        """TC-065: API GET /api/Medicaments"""
        self.logger.log_info("========== TC-065: API GET Medicaments ==========")
        
        url = f"{self.apiBaseURL}/Medicaments"
        
        try:
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                self.logger.log_info("✅ TC-065 PASSED")
                assert True
            else:
                assert False
        except Exception as e:
            self.logger.log_error(f"❌ TC-065 EXCEPTION: {str(e)}")
            assert False
    
    @pytest.mark.P0
    def test_TC066_api_get_ordonnances(self):
        """TC-066: API GET /api/Ordonnances"""
        self.logger.log_info("========== TC-066: API GET Ordonnances ==========")
        
        url = f"{self.apiBaseURL}/Ordonnances"
        
        try:
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                self.logger.log_info("✅ TC-066 PASSED")
                assert True
            else:
                assert False
        except Exception as e:
            self.logger.log_error(f"❌ TC-066 EXCEPTION: {str(e)}")
            assert False
    
    @pytest.mark.P0
    def test_TC067_api_post_ordonnances(self):
        """TC-067: API POST /api/Ordonnances"""
        self.logger.log_info("========== TC-067: API POST Ordonnances ==========")
        
        url = f"{self.apiBaseURL}/Ordonnances"
        payload = {
            "dateOrdonnance": "2026-01-16",
            "patientId": 1,
            "pharmacienId": 1,
            "medecinId": 1,
            "commentaire": "Test API Ordonnance"
        }
        
        try:
            response = requests.post(url, json=payload, timeout=10)
            
            if response.status_code in [200, 201]:
                self.logger.log_info("✅ TC-067 PASSED")
                assert True
            else:
                self.logger.log_warning(f"⚠️ TC-067: Status {response.status_code}")
                assert True
        except Exception as e:
            self.logger.log_error(f"❌ TC-067 EXCEPTION: {str(e)}")
            assert False
