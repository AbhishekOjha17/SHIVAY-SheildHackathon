/**
 * Shared TypeScript types for emergency cases
 */

export enum EmergencyStatus {
  OPEN = "open",
  DISPATCHED = "dispatched",
  IN_PROGRESS = "in_progress",
  RESOLVED = "resolved",
  CANCELLED = "cancelled",
}

export enum SeverityLevel {
  CRITICAL = "critical",
  HIGH = "high",
  MEDIUM = "medium",
  LOW = "low",
}

export enum EmergencyType {
  ACCIDENT = "accident",
  MEDICAL = "medical",
  FIRE = "fire",
  CRIME = "crime",
  NATURAL_DISASTER = "natural_disaster",
  OTHER = "other",
}

export interface Location {
  lat: number;
  lng: number;
  address?: string;
}

export interface EmergencyCase {
  case_id: string;
  caller_id?: string;
  emergency_type: EmergencyType;
  severity_level: SeverityLevel;
  status: EmergencyStatus;
  location: Location;
  description?: string;
  created_at: string;
  updated_at: string;
}

