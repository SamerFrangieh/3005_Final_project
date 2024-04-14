CREATE TABLE auth_permission (
    id integer,
    content_type_id integer,
    codename character varying,
    name character varying
);

CREATE TABLE django_content_type (
    id integer,
    model character varying,
    app_label character varying
);

CREATE TABLE auth_group (
    id integer,
    name character varying
);

CREATE TABLE auth_user (
    id integer,
    date_joined timestamp with time zone,
    is_active boolean,
    password character varying,
    username character varying,
    first_name character varying,
    email character varying,
    last_login timestamp with time zone,
    is_staff boolean,
    last_name character varying,
    is_superuser boolean
);

CREATE TABLE myapp_room (
    room_id integer,
    name character varying
);

CREATE TABLE myapp_trainer (
    trainer_id integer,
    password character varying,
    name character varying
);

CREATE TABLE myapp_member (
    member_id integer,
    fitness_goal character varying,
    systolic_bp integer,
    act_levels character varying,
    name character varying,
    age numeric,
    height numeric,
    weight numeric,
    weeks_to_goal integer,
    password character varying,
    diastolic_bp integer,
    goal_weight numeric,
    health_metrics jsonb
);

CREATE TABLE myapp_admin (
    admin_id integer,
    name character varying,
    password character varying
);

CREATE TABLE myapp_service (
    id bigint,
    service_name character varying,
    price numeric
);

CREATE TABLE myapp_equipmentmaintenance (
    equipment_id integer,
    name character varying,
    status character varying,
    last_maintenance_date date,
    next_maintenance_date date
);
CREATE TABLE auth_user_groups (
    id bigint,
    group_id integer,
    user_id integer
);

CREATE TABLE auth_group_permissions (
    id bigint,
    permission_id integer,
    group_id integer
);

CREATE TABLE auth_user_user_permissions (
    id bigint,
    permission_id integer,
    user_id integer
);

CREATE TABLE django_admin_log (
    id integer,
    change_message text,
    user_id integer,
    object_id text,
    content_type_id integer,
    object_repr character varying,
    action_time timestamp with time zone,
    action_flag smallint
);

CREATE TABLE myapp_billing (
    id bigint,
    due_date date,
    status character varying,
    member_id integer,
    amount_due numeric
);

CREATE TABLE myapp_roombooking (
    room_booking_id integer,
    start_time timestamp with time zone,
    room_id integer,
    end_time timestamp with time zone
);

CREATE TABLE myapp_groupfitnessclass (
    group_fitness_class_id integer,
    date date,
    room_id integer,
    trainer_id integer,
    end_time time without time zone,
    start_time time without time zone
);

CREATE TABLE myapp_personalsession (
    personal_session_id integer,
    start_time time without time zone,
    end_time time without time zone,
    trainer_id integer,
    member_id integer,
    date date
);

CREATE TABLE myapp_traineravailability (
    id bigint,
    trainer_id integer,
    day_of_week integer,
    check_out time without time zone,
    check_in time without time zone
);

CREATE TABLE myapp_membergroupfitnessregistration (
    id bigint,
    registration_date date,
    group_fitness_class_id integer,
    member_id integer
);

CREATE TABLE myapp_payment (
    id bigint,
    payment_method character varying,
    payment_status character varying,
    payment_date date,
    billing_id bigint
);

CREATE TABLE django_session (
    expire_date timestamp with time zone,
    session_key character varying,
    session_data text
);

CREATE TABLE django_migrations (
    id bigint,
    app character varying,
    name character varying,
    applied timestamp with time zone
);
