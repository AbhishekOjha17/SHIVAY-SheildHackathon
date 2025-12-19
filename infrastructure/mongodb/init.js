// MongoDB initialization script
db = db.getSiblingDB('shivay_emergency');

// Create collections with indexes
db.createCollection('Emergency_Cases');
db.createCollection('Caller_Transcripts');
db.createCollection('Hospital_Resources');
db.createCollection('Ambulance_Live_Tracking');
db.createCollection('Police_Officer_Actions');
db.createCollection('AI_Recommendations');
db.createCollection('Location_Metadata');

// Create indexes
db.Emergency_Cases.createIndex({ case_id: 1 }, { unique: true });
db.Emergency_Cases.createIndex({ status: 1 });
db.Emergency_Cases.createIndex({ severity_level: 1 });
db.Emergency_Cases.createIndex({ created_at: -1 });

db.Caller_Transcripts.createIndex({ case_id: 1 });
db.Caller_Transcripts.createIndex({ call_id: 1 });

db.Hospital_Resources.createIndex({ hospital_id: 1 }, { unique: true });
db.Hospital_Resources.createIndex({ is_active: 1 });

db.Ambulance_Live_Tracking.createIndex({ ambulance_id: 1 }, { unique: true });
db.Ambulance_Live_Tracking.createIndex({ status: 1 });
db.Ambulance_Live_Tracking.createIndex({ assigned_case: 1 });

db.Police_Officer_Actions.createIndex({ case_id: 1 });
db.Police_Officer_Actions.createIndex({ officer_id: 1 });

db.AI_Recommendations.createIndex({ case_id: 1 });
db.AI_Recommendations.createIndex({ recommendation_id: 1 }, { unique: true });

print('Database initialized successfully');

