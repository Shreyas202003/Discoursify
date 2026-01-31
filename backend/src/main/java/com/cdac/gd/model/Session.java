package com.cdac.gd.model;

import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDateTime;
import java.util.UUID;

@Data
@Entity
@Table(name = "sessions")
public class Session {
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;

    private String topic;
    private String hostId;
    private LocalDateTime startTime;
    private LocalDateTime endTime;
    private String status; // SCHEDULED, LIVE, COMPLETED

    @Column(columnDefinition = "text")
    private String description;

    // New fields for session management
    private String type; // PUBLIC, PRIVATE
    private String code; // 6-digit join code
    private Integer timeLimit; // in minutes
    private Boolean hasWaitingRoom;
    private String hostEmail;

    private Integer maxParticipants;
    private String hostRole; // "PARTICIPANT" or "OBSERVER"

    @ElementCollection
    private java.util.List<String> transcript;

    private Integer participantsCount;

    @ElementCollection
    private java.util.List<Participant> participants;

    @ElementCollection
    private java.util.List<Participant> waitingList;
}
